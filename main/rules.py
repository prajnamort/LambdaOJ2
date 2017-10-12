import rules


is_faculty = rules.is_group_member('faculty')
can_access_media_files = is_faculty | rules.is_superuser
has_faculty_privilege = is_faculty | rules.is_superuser
can_access_unreleased_problems = has_faculty_privilege

@rules.predicate
def can_access_problem(user, problem):
    return problem.released or can_access_unreleased_problems(user)

@rules.predicate
def can_view_submit(user, submit):
    return has_faculty_privilege(user) or submit.user == user


rules.add_rule('is_faculty', is_faculty)
rules.add_rule('can_access_media_files', can_access_media_files)
rules.add_rule('can_access_unreleased_problems', can_access_unreleased_problems)
rules.add_rule('can_access_problem', can_access_problem)
rules.add_rule('can_view_submit', can_view_submit)
