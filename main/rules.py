import rules


is_faculty = rules.is_group_member('faculty')
has_faculty_privilege = is_faculty | rules.is_superuser
can_access_unreleased_problems = has_faculty_privilege

@rules.predicate
def can_access_problem(user, problem):
    return problem.released or can_access_unreleased_problems(user)


rules.add_rule('is_faculty', is_faculty)
rules.add_rule('can_access_unreleased_problems', can_access_unreleased_problems)
rules.add_rule('can_access_problem', can_access_problem)
