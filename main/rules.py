import rules


is_faculty = rules.is_group_member('faculty')
has_faculty_privilege = is_faculty | rules.is_superuser


rules.add_rule('can_access_unreleased_problems',
               rules.is_authenticated & has_faculty_privilege)  # TODO: is_authenticated
