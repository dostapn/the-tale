# coding: utf-8


from the_tale.game.postponed_tasks import ComplexChangeTask


class CardsTestMixin(object):

    def use_attributes(self, hero_id, place_id=None, step=ComplexChangeTask.STEP.LOGIC, storage=None, highlevel=None, critical=False):
        data = {'data': {'hero_id': hero_id},
                'step': step,
                'main_task_id': 0,
                'storage': storage}

        if place_id is not None:
            data['data']['place_id'] = place_id

        if highlevel is not None:
            data['highlevel'] = highlevel

        return data