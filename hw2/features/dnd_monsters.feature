Feature: DnD Monsters
  As player,
  I want to know the current hp or hit-points that a monster has
  So that I can access what move to do next

  Scenario Outline: DnD Monster Hit-Points
    When the DnD API is queried with "<monster>"
    Then the response status code is 200
    And the response shows hit_points of "<hp>"

    Examples: Hit-Points
      | monster             | hp    |
      | adult-black-dragon  | 195   |
      | chimera             | 114   |
      | shield-guardian     | 142   |