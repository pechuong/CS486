Feature: DnD Classes
  As player,
  I want to know how many hits a character/class can take before dying
  So that I can decide which character to play(even though this is a bad way of choosing)

  Scenario Outline: DnD Classes Hit-Die
    When the DnD API is queried with "<classes>"
    Then the response status code is 200
    And the response shows hit_die of "<hit>"

    Examples: Hit-Die
      | classes      | hit   |
      | paladin      | 10    |
      | ranger       | 10    |
      | barbarian    | 12    |
