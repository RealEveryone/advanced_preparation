import unittest

from project.team import Team


class TestTeam(unittest.TestCase):

    def test__init__method_for_proper_initialization(self):
        test_team = Team('Name')
        self.assertEqual(test_team.name, 'Name')
        self.assertDictEqual(test_team.members, {})

    def test__name_setter__when_given_non_alpha_char(self):
        with self.assertRaises(ValueError) as ex:
            Team('*')
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")

    def test__add_member__method_append_members_to_members_attribute__return_str(self):
        test_team = Team('Name')
        result = test_team.add_member(Name1=20, Name2=21, Name3=22)
        self.assertDictEqual(test_team.members, {'Name1': 20, 'Name2': 21, 'Name3': 22})
        self.assertEqual(result, 'Successfully added: Name1, Name2, Name3')

    def test__remove_member__method_when_member_exists__remove_member_from_members_dict(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20, Name2=21, Name3=22)
        result = test_team.remove_member('Name1')
        self.assertEqual(result, "Member Name1 removed")
        self.assertDictEqual(test_team.members, {'Name2': 21, 'Name3': 22})

    def test__remove_member__method_when_member_does_not_exists__expect_str(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20, Name2=21, Name3=22)
        result = test_team.remove_member('Name4')
        self.assertEqual(result, "Member with name Name4 does not exist")

    def test__len__method(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20, Name2=21, Name3=22)
        result = len(test_team)
        self.assertEqual(result, 3)

    def test__gt__method_true(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20, Name2=21, Name3=22)
        test_team2 = Team('NameOne')
        test_team2.add_member(Name1=20, Name2=21)
        self.assertTrue(test_team > test_team2)

    def test__gt__method_false(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20)
        test_team2 = Team('NameOne')
        test_team2.add_member(Name1=20, Name2=21)
        self.assertFalse(test_team > test_team2)

    def test__add__method_join_two_teams(self):
        test_team = Team('Name')
        test_team.add_member(Name1=20, Name2=21, Name3=22)
        test_team2 = Team('NameOne')
        test_team2.add_member(Name4=20, Name5=21)
        new_team = test_team + test_team2
        self.assertDictEqual(new_team.members, {'Name1': 20, 'Name2': 21, 'Name3': 22, 'Name4': 20, 'Name5': 21})

    def test__str__(self):
        test_team2 = Team('NameOne')
        test_team2.add_member(Name4=20)
        self.assertEqual(str(test_team2), 'Team name: NameOne\nMember: Name4 - 20-years old')

if __name__ == '__main__':
    unittest.main()