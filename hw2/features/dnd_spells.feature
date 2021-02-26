Feature: DnD Spells
  As player,
  I want to know the casting time of a spell
  so that I know when in advance to use the spell

  Scenario Outline: DnD Spells Cast-Time
    When the DnD API is queried with "<spell>"
    Then the response status code is 200
    And the response shows cast time of "<cast_time>"

    Examples: Hit-Die
      | spell       | cast_time   |
      | acid-splash | 1 action    |
      | blight      | 1 action    |
      | teleport    | 1 action    |
