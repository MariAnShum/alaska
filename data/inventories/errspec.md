# Спецификация ошибок

_написана с опорой на инструкцию №3 v4_

Код ошибки/предупреждения состоит из трех частей:

1. Буква означает тип: ошибка (явное нарушение правила) или предупреждение (ошибка очень вероятна, но убедиться можно, только послушав медиафайл).
2. Число до точки означает номер нарушенного правила в инструкции.
3. Число после точки означает вариант нарушения. Присутствует, даже когда вариант единственный; это нужно на тот случай, если впоследствии найдутся еще варианты нарушения этого правила.

В фигурных скобках записываются мои комментарии.

## Ошибки

E0.1: При написании использованы не предусмотренные буквы.

{Напр. _j_.}

E2.1: Безударный гласный обозначен буквой _o_.

E2.2: Во многосложном слове более одного раза встречается _o_.

{Отмечается, если в слове не поставлено ударение.}

E2.3: Безударный гласный обозначен буквой _e_.

{При проверке E2.1 и E3.1 учитываются совместно.}

E2.4: Во многосложном слове более одного раза встречается _e_.

{Отмечается, если в слове не поставлено ударение. При проверке E2.2 и E3.2 учитываются совместно.}

E3.1: Отсутствует знак палатализации после согласного (не _l_) перед _i_.

E3.2: Поставлен знак палатализации перед _i_ после _ch_, _sh_,  _y_ или _zh_.

E3.3: Отсутствует знак палатализации перед _e_ после губного (_b_, _p_, _f_, _w_) или зубного смычного (_t_, _d_, _n_).

E3.4: Поставлен знак палатализации перед _e_ после любого согласного, кроме _b_, _p_, _f_, _w_, _t_, _d_, _n_.

E5.1: Использовано сочетание любого гласного с _i_ (с ударением или без).

E7.1: Использован дефис.

E8.1: Отрицание записано как _n'e_ (правильно: _n'i_  или, в редких случаях, _n'é_).

E9.1: Во многосложном слове отсутствует ударение.

E9.2: Во многосложном слове поставлено более одного ударения.

## Предупреждения

W1.1: Вероятно, ошибочно использовано сочетание букв _sch_, _sh_ либо _shch_.

W6.1: Вероятно, вместо знака мягкости после палатализованного согласного перед гласным использована буква y.

{Вынесено в предупреждения, так как использование _y_ между согласным и гласным может быть верным, например в _syel_ "съел".}

W10.1: Встречено односложное слово с ударением. Требуется проверка синтагмы.

{Если синтагма данного слова состоит исключительно из односложных безударных русских слов, то постановка ударения оправдана, иначе это расценивается как ошибка.}

## Что пока автоматически проверить нельзя

4: все, что касается этого правила.

6: случаи, когда не обозначена палатализация между мягким согласным и непередним гласным; отмечаются как ошибки случаи, когда i или e следует без ' за одним из согласных, которые не бывают мягкими (zh, sh, ch, ts).

7: слитность энклитик и раздельность проклитик.

8: оглушение предлога.

9: слитное написание многосложной клитики с опорным словом, как следствие -- отсутствие ударения на клитике.

10: все, что касается этого правила.
