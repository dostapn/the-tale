# coding: utf-8

from utg.words import WordForm, Word, Properties
from utg.relations import WORD_TYPE
from utg.data import VERBOSE_TO_PROPERTIES
from utg.dictionary import Dictionary

from the_tale.linguistics.lexicon import exceptions


def noun(forms, properties, countable=None):

    if (len(forms) == 12):
        forms = forms + forms[6:]

    properties = Properties(*[VERBOSE_TO_PROPERTIES[prop.strip()] for prop in properties.split(',')])

    if len(forms) != Word.get_forms_number(type=WORD_TYPE.NOUN):
        raise exceptions.WrongFormNumberError()

    return WordForm(Word(type=WORD_TYPE.NOUN, forms=forms, properties=properties))


def text(form):
    return WordForm(Word(type=WORD_TYPE.TEXT, forms=[form], properties=Properties()))


forms = [ noun([u'герой', u'героя', u'герою', u'героя', u'героем', u'герое',
                u'герои', u'героев', u'героям', u'героев', u'героями', u'героях'], u'од,мр'),
          noun([u'привидение', u'привидения', u'привидению', u'привидение', u'привидением', u'привидении',
                u'привидения', u'привидений', u'привидениям', u'привидения', u'привидениями', u'привидениях'], u'од,ср'),
          noun([u'героиня', u'героини', u'героине', u'героиню', u'героиней', u'героине',
                u'героини', u'героинь', u'героиням', u'героинь', u'героинями', u'героинях'], u'од,жр'),
          noun([u'рыцарь', u'рыцаря', u'рыцарю', u'рыцаря', u'рыцарем', u'рыцаре',
                u'рыцари', u'рыцарей', u'рыцарям', u'рыцарей', u'рыцарями', u'рыцарях'], u'од,мр'),
          noun([u'призрак', u'призрака', u'призраку', u'призрака', u'призраком', u'призраке',
                u'призраки', u'призраков', u'призракам', u'призраков', u'призраками', u'призраках'], u'од,мр'),
          noun([u'чудовище', u'чудовища', u'чудовищу', u'чудовище', u'чудовищем', u'чудовище',
                u'чудовища', u'чудовищ', u'чудовищам', u'чудовищ', u'чудовищами', u'чудовищах'], u'од,ср'),
          noun([u'русалка', u'русалки', u'русалке', u'русалку', u'русалкой', u'русалке',
                u'русалки', u'русалок', u'русалкам', u'русалок', u'русалками', u'русалках'], u'од,жр'),
          noun([u'боец', u'бойца', u'бойцу', u'бойца', u'бойцом', u'бойце',
                u'бойцы', u'бойцов', u'бойцам', u'бойцов', u'бойцами', u'бойцах'], u'од,мр'),
          noun([u'жираф', u'жирафа', u'жирафу', u'жирафа', u'жирафом', u'жирафе',
                u'жирафы', u'жирафов', u'жирафам', u'жирафов', u'жирафами', u'жирафах'], u'од,мр'),
          noun([u'чучело', u'чучела', u'чучелу', u'чучело', u'чучелом', u'чучеле',
                u'чучела', u'чучел', u'чучелам', u'чучела', u'чучелами', u'чучелах'], u'но,ср'),
          noun([u'зебра', u'зебры', u'зебре', u'зебру', u'зеброй', u'зебре',
                u'зебры', u'зебр', u'зебрам', u'зебр', u'зебрами', u'зебрах'], u'од,жр'),
          noun([u'слон', u'слана', u'слону', u'слона', u'слоном', u'слоне',
                u'слоны', u'слонов', u'слонам', u'слонов', u'слонами', u'слонах'], u'од,мр'),
          noun([u'гусь', u'гуся', u'гусю', u'гуся', u'гусем', u'гусе',
                u'гуси', u'гусей', u'гусям', u'гусей', u'гусями', u'гусях'], u'од,мр'),
          noun([u'пугало', u'пугала', u'пугалу', u'пагуло', u'пугалом', u'пунале',
                u'пугала', u'пугалах', u'пугалам', u'пугала', u'пугалами', u'пугалах'], u'од,ср'),
          noun([u'свинья', u'свиньи', u'свинье', u'свинью', u'свиньёй', u'свинье',
                u'свиньи', u'свиней', u'свиньям', u'свиней', u'свиньями', u'свиньях'], u'од,жр'),
          noun([u'волк', u'волка', u'волку', u'волка', u'волком', u'волке',
                u'волки', u'волков', u'волкам', u'волков', u'волками', u'волках'], u'од,мр'),
          noun([u'Минск', u'Минска', u'Минску', u'Минск', u'Минском', u'Минске',
                u'', u'', u'', u'', u'', u''], u'но,мр,ед'),
          noun([u'Простоквашино', u'Простоквашина', u'Простоквашину', u'Простоквашино', u'Простоквашином', u'Простоквашине',
                u'', u'', u'', u'', u'', u''], u'но,ср,ед'),
          noun([u'Вилейка', u'Вилейки', u'Вилейке', u'Вилейку', u'Вилейкой', u'Вилейке',
                u'', u'', u'', u'', u'', u''], u'но,жр,ед'),
          noun([u'', u'', u'', u'', u'', u'',
                u'Барановичи', u'Барановичей', u'Барановичам', u'Барановичи', u'Барановичами', u'Барановичах'], u'но,мн'),
          noun([u'Тагил', u'Тагила', u'Тагилу', u'Тагил', u'Тагилом', u'Тагиле',
                u'', u'', u'', u'', u'', u''], u'од,мр,ед'),
          noun([u'Чугуево', u'Чугуева', u'Чугуеву', u'Чугуево', u'Чугуевом', u'Чугуеве',
                u'', u'', u'', u'', u'', u''], u'но,ср,ед'),
          noun([u'Рига', u'Риги', u'Риге', u'Ригу', u'Ригой', u'Риге',
                u'', u'', u'', u'', u'', u''], u'од,жр,ед'),
          noun([u'', u'', u'', u'', u'', u'',
                u'Афины', u'Афин', u'Афинам', u'Афины', u'Афинами', u'Афинах'], u'но,мн'),
          noun([u'Магадан', u'Магадана', u'Магадану', u'Магадан', u'Магаданом', u'Магадане',
                u'', u'', u'', u'', u'', u''], u'но,мр,ед'),
          noun([u'Бородино', u'Бородина', u'Бородину', u'Бородино', u'Бородином', u'Бородине',
                u'', u'', u'', u'', u'', u''], u'но,ср,ед'),
          noun([u'Уфа', u'Уфы', u'Уфе', u'Уфу', u'Уфой', u'Уфе',
                u'', u'', u'', u'', u'', u''], u'но,жр,ед'),
          noun([u'', u'', u'', u'', u'', u'',
                u'Чебоксары', u'Чебоксар', u'Чебоксарам', u'Чебоксары', u'Чебоксарами', u'Чебоксарах'], u'но,мн'),
          noun([u'нож', u'ножа', u'ножу', u'нож', u'ножом', u'ноже',
                u'ножи', u'ножей', u'ножам', u'ножи', u'ножами', u'ножах'], u'но,мр'),
          noun([u'ядро', u'ядра', u'ядру', u'ядро', u'ядром', u'ядре',
                u'ядра', u'ядер', u'ядрам', u'ядра', u'ядрами', u'ядрах'], u'но,ср'),
          noun([u'пепельница', u'пепельницы', u'пепельнице', u'пепельницу', u'пепельницей', u'пепельнице',
                u'пепельницы', u'пепельниц', u'пепельницам', u'пепельницы', u'пепельницами', u'пепельниц'], u'но,жр'),
          noun([u'', u'', u'', u'', u'', u'',
                u'ножницы', u'ножниц', u'ножницам', u'ножницы', u'ножницами', u'ножницах'], u'но,мн'),
          noun([u'кинжал', u'кинжала', u'кинжалу', u'кинжал', u'кинжалом', u'кинжале',
                u'кинжалы', u'кинжалов', u'кинжалам', u'кинжалы', u'кинжалами', u'кинжалах'], u'но,мр'),
          noun([u'окно', u'окна', u'окну', u'окно', u'окном', u'окне',
                u'окна', u'окон', u'окнам', u'окна', u'окнами', u'окнах'], u'но,ср'),
          noun([u'мечта', u'мечты', u'мечте', u'мечту', u'мечтой', u'мечте',
                u'мечты', u'мечт', u'мечтам', u'мечты', u'мечтами', u'мечтах'], u'но,жр'),
          noun([u'', u'', u'', u'', u'', u'',
                u'макароны', u'макарон', u'макаронам', u'макароны', u'макаронами', u'макаронами'], u'но,мн'),
          noun([u'меч', u'меча', u'мечу', u'меч', u'мечом', u'мече',
                u'мечи', u'мечей', u'мечам', u'мечи', u'мечами', u'мечах'], u'но,мр'),
          noun([u'варенье', u'варенья', u'варенью', u'варенье', u'вареньем', u'варенье',
                u'вареньях', u'варений', u'вареньям', u'варенья', u'вареньями', u'вареньях'], u'но,ср'),
          noun([u'чашка', u'чашки', u'чашке', u'чашку', u'чашкой', u'чашке',
                u'чашки', u'чашке', u'чашкам', u'чашки', u'чашками', u'чашках'], u'но,жр'),
          noun([u'', u'', u'', u'', u'', u'',
                u'дрова', u'дров', u'дровам', u'дрова', u'дровами', u'дровах'], u'но,мн'),
          noun([u'форт', u'форта', u'форту', u'форт', u'фортом', u'форте',
                u'форты', u'фортов', u'фортам', u'форты', u'фортами', u'фортах'], u'но,мр'),
          noun([u'захолустье', u'захолустья', u'захолустью', u'захолустье', u'захолустьем', u'захолустье',
                u'захолустья', u'захолустий', u'захолустьям', u'захолустья', u'захолустьями', u'захолустий'], u'но,ср'),
          noun([u'святыня', u'святыни', u'святыне', u'святыню', u'святыней', u'святыне',
                u'святыни', u'святынь', u'святыням', u'святыне', u'святынями', u'святынях'], u'но,жр'),
          noun([u'мемориал', u'мемориала', u'мемориалу', u'мемориал', u'мемориалом', u'мемориала',
                u'мемориалы', u'мемориалов', u'мемориалам', u'мемориалы', u'мемориалами', u'мемориалах'], u'но,мр'),
          noun([u'замок', u'замка', u'замку', u'замок', u'замком', u'замке',
                u'замки', u'замков', u'замкам', u'замки', u'замками', u'замках'], u'но,мр'),
          noun([u'пристанище', u'пристанища', u'пристанищу', u'пристанище', u'пристанищем', u'пристанище',
                u'пристанища', u'пристанищ', u'пристанища', u'пристанища', u'пристанищами', u'пристанищах'], u'но,ср'),
          noun([u'земля', u'земли', u'земле', u'землю', u'землёй', u'земле',
                u'земли', u'земель', u'землям', u'земли', u'землями', u'землях'], u'но,жр'),
          noun([u'колония', u'колонии', u'колонии', u'колонию', u'колонией', u'колонии',
                u'колонии', u'колоний', u'колониям', u'колонии', u'колониями', u'колониях'], u'но,жр'),
          noun([u'человек', u'человека', u'человеку', u'человека', u'человеком', u'человеке',
                u'люди', u'людей', u'людям', u'людей', u'людьми', u'людях',
                u'человек', u'человек', u'человекам', u'человек', u'человеками', u'человеках'], u'од,мр'),
          noun([u'эльф', u'эльфа', u'эльфу', u'эльфа', u'эльфом', u'эльфе',
                u'эльфы', u'эльфов', u'эльфам', u'эльфов', u'эльфами', u'эльфах'], u'од,мр'),
          noun([u'орк', u'орка', u'орку', u'орка', u'орком', u'орке',
                u'орки', u'орков', u'оркам', u'орков', u'орками', u'орках'], u'од,мр'),
          noun([u'гоблин', u'гоблина', u'гоблину', u'гоблина', u'гоблином', u'гоблине',
                u'гоблины', u'гоблинов', u'гоблинам', u'гоблинов', u'гоблинами', u'гоблинах'], u'од,мр'),
          noun([u'дварф', u'дварфа', u'дварфу', u'дварфа', u'дварфом', u'дварфе',
                u'дварфы', u'дварфов', u'дварфам', u'дварфов', u'дварфами', u'дварфах'], u'од,мр'),
          text(u'любой текст'),
          text(u'текст текст текст'),
          text(u'какой-то текст')
                 ]


DICTIONARY = Dictionary(words=[form.word for form in forms])
