from django_seed import Seed

seeder = Seed.seeder('ru_RU')

from mainapp.models import TermCourses
seeder.add_entity(TermCourses, 5)


inserted_pks = seeder.execute()
