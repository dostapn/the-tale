# coding: utf-8
import mock

from common.utils import testcase

from accounts.logic import register_user
from game.heroes.prototypes import HeroPrototype
from game.logic_storage import LogicStorage


from game.balance import formulas as f, constants as c, enums as e

from game.logic import create_test_map
from game.actions.prototypes import ActionMoveToPrototype, ActionInPlacePrototype, ActionRestPrototype
from game.actions.prototypes import ActionResurrectPrototype, ActionBattlePvE1x1Prototype, ActionRegenerateEnergyPrototype
from game.prototypes import TimePrototype

class MoveToActionTest(testcase.TestCase):

    def setUp(self):
        super(MoveToActionTest, self).setUp()

        self.p1, self.p2, self.p3 = create_test_map()

        result, account_id, bundle_id = register_user('test_user')

        self.hero = HeroPrototype.get_by_account_id(account_id)
        self.storage = LogicStorage()
        self.storage.add_hero(self.hero)
        self.action_idl = self.hero.actions.current_action

        self.hero.position.set_place(self.p1)

        self.action_move = ActionMoveToPrototype.create(hero=self.hero, destination=self.p3)


    def tearDown(self):
        pass

    def test_create(self):
        self.assertEqual(self.action_idl.leader, False)
        self.assertEqual(self.action_move.leader, True)
        self.assertEqual(self.action_move.bundle_id, self.action_idl.bundle_id)
        self.storage._test_save()


    def test_processed(self):
        self.hero.position.set_place(self.p3)
        self.storage.process_turn()
        self.assertEqual(len(self.hero.actions.actions_list), 1)
        self.assertEqual(self.hero.actions.current_action, self.action_idl)
        self.storage._test_save()


    @mock.patch('game.map.places.prototypes.PlacePrototype.safety', 1.0)
    def test_not_ready(self):
        self.storage.process_turn()
        self.assertEqual(len(self.hero.actions.actions_list), 2)
        self.assertEqual(self.hero.actions.current_action, self.action_move)
        self.assertTrue(self.hero.position.road)
        self.storage._test_save()


    def test_full_move(self):

        current_time = TimePrototype.get_current_time()

        while self.hero.position.place is None or self.hero.position.place.id != self.p3.id:
            self.storage.process_turn()
            current_time.increment_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionInPlacePrototype.TYPE)
        self.storage._test_save()

    def test_full(self):

        current_time = TimePrototype.get_current_time()

        while not self.action_idl.leader:
            self.storage.process_turn()
            current_time.increment_turn()

        self.storage._test_save()

    @mock.patch('game.map.places.prototypes.PlacePrototype.safety', 1.0)
    def test_modify_speed_in_transport_node(self):

        from game.map.places.modifiers.prototypes import TransportNode

        self.hero.position.place.modifier = TransportNode(self.hero.position.place)

        with mock.patch('game.heroes.prototypes.HeroPositionPrototype.modify_move_speed',
                        mock.Mock(return_value=self.hero.move_speed)) as speed_modifier_call_counter:
            self.storage.process_turn()

        self.assertEqual(speed_modifier_call_counter.call_count, 1)

    @mock.patch('game.map.places.prototypes.PlacePrototype.safety', 1.0)
    def test_short_teleport(self):

        current_time = TimePrototype.get_current_time()

        self.storage.process_turn()

        old_road_percents = self.hero.position.percents
        self.action_move.short_teleport(1)
        self.assertTrue(old_road_percents < self.hero.position.percents)

        self.action_move.short_teleport(self.hero.position.road.length)
        self.assertEqual(self.hero.position.percents, 1)
        self.assertTrue(self.action_move.updated)

        current_time.increment_turn()
        self.storage.process_turn()

        self.assertEqual(self.hero.position.place.id, self.p2.id)

        self.storage._test_save()


    @mock.patch('game.map.places.prototypes.PlacePrototype.safety', 0.0)
    def test_battle(self):
        self.storage.process_turn()
        self.assertEqual(self.hero.actions.current_action.TYPE, ActionBattlePvE1x1Prototype.TYPE)
        self.storage._test_save()


    def test_rest(self):
        self.hero.health = 1
        self.action_move.state = self.action_move.STATE.BATTLE
        self.storage.process_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionRestPrototype.TYPE)

        self.storage._test_save()

    def test_regenerate_energy_on_move(self):
        self.hero.preferences.energy_regeneration_type = e.ANGEL_ENERGY_REGENERATION_TYPES.PRAY
        self.hero.last_energy_regeneration_at_turn -= max([f.angel_energy_regeneration_delay(energy_regeneration_type)
                                                           for energy_regeneration_type in c.ANGEL_ENERGY_REGENERATION_STEPS.keys()])
        self.action_move.state = self.action_move.STATE.CHOOSE_ROAD

        self.storage.process_turn()
        current_time = TimePrototype.get_current_time()
        current_time.increment_turn()
        self.storage.process_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionRegenerateEnergyPrototype.TYPE)

        self.storage._test_save()

    def test_not_regenerate_energy_on_move_for_sacrifice(self):
        self.hero.preferences.energy_regeneration_type = e.ANGEL_ENERGY_REGENERATION_TYPES.SACRIFICE
        self.hero.last_energy_regeneration_at_turn -= max([f.angel_energy_regeneration_delay(energy_regeneration_type)
                                                           for energy_regeneration_type in c.ANGEL_ENERGY_REGENERATION_STEPS.keys()])
        self.action_move.state = self.action_move.STATE.CHOOSE_ROAD

        self.storage.process_turn()
        current_time = TimePrototype.get_current_time()
        current_time.increment_turn()
        self.storage.process_turn()


        self.assertNotEqual(self.hero.actions.current_action.TYPE, ActionRegenerateEnergyPrototype.TYPE)

        self.storage._test_save()

    def test_regenerate_energy_after_battle_for_sacrifice(self):
        self.hero.preferences.energy_regeneration_type = e.ANGEL_ENERGY_REGENERATION_TYPES.SACRIFICE
        self.hero.last_energy_regeneration_at_turn -= max([f.angel_energy_regeneration_delay(energy_regeneration_type)
                                                           for energy_regeneration_type in c.ANGEL_ENERGY_REGENERATION_STEPS.keys()])
        self.action_move.state = self.action_move.STATE.BATTLE

        self.storage.process_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionRegenerateEnergyPrototype.TYPE)

        self.storage._test_save()

    def test_resurrect(self):
        self.hero.kill()
        self.action_move.state = self.action_move.STATE.BATTLE
        self.storage.process_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionResurrectPrototype.TYPE)
        self.storage._test_save()


    @mock.patch('game.map.places.prototypes.PlacePrototype.safety', 1.0)
    def test_inplace(self):

        current_time = TimePrototype.get_current_time()

        self.storage.process_turn()
        self.hero.position.percents = 1

        current_time.increment_turn()
        self.storage.process_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionInPlacePrototype.TYPE)
        self.storage._test_save()


class MoveToActionWithBreaksTest(testcase.TestCase):

    def setUp(self):
        super(MoveToActionWithBreaksTest, self).setUp()
        self.p1, self.p2, self.p3 = create_test_map()

        result, account_id, bundle_id = register_user('test_user')

        self.hero = HeroPrototype.get_by_account_id(account_id)
        self.storage = LogicStorage()
        self.storage.add_hero(self.hero)
        self.action_idl = self.hero.actions.current_action


        self.hero.position.set_place(self.p1)

        self.action_move = ActionMoveToPrototype.create(hero=self.hero, destination=self.p3, break_at=0.75)

    def test_sequence_move(self):

        current_time = TimePrototype.get_current_time()

        while self.hero.actions.current_action != self.action_idl:
            self.storage.process_turn()
            current_time.increment_turn()

        self.assertEqual(self.hero.position.road.point_1_id, self.p2.id)
        self.assertEqual(self.hero.position.road.point_2_id, self.p3.id)

        ActionMoveToPrototype.create(hero=self.hero, destination=self.p1, break_at=0.9)
        while self.hero.actions.current_action != self.action_idl:
            self.storage.process_turn()
            current_time.increment_turn()

        self.assertEqual(self.hero.position.road.point_1_id, self.p1.id)
        self.assertEqual(self.hero.position.road.point_2_id, self.p2.id)

        ActionMoveToPrototype.create(hero=self.hero, destination=self.p2)
        while self.hero.position.place is None or self.hero.position.place.id != self.p2.id:
            self.storage.process_turn()
            current_time.increment_turn()

        self.assertEqual(self.hero.actions.current_action.TYPE, ActionInPlacePrototype.TYPE)
        self.storage._test_save()
