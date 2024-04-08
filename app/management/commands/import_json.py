import json
from django.core.management.base import BaseCommand
from app.models import Data


class Command(BaseCommand):
    help = 'Import external JSON file data into django database'

    def handle(self,*args,**kwargs):
        with open(r'----file_path-----','r',encoding='utf8') as file:
            data=json.load(file)
            print(data)             

            for item in data:                
                Data.objects.create(
                    sector=item.get('sector'),
                    topic=item.get('topic'),
                    insight=item.get('insight'),
                    region=item.get('region'),
                )
        self.stdout.write(self.style.SUCCESS('Done'))
