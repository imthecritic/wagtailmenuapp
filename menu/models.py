from django.db import models

from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel, MultiFieldPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailcore.models import Orderable,Page
from modelcluster.fields import ForeignKey, ParentalKey
from modelcluster.models import ClusterableModel



class menu_item(models.Model):
    page_url = models.URLField(null=True, blank=True)
    menu_text = models.CharField(max_length = 150)
    internal_link = models.ForeignKey( 'wagtailcore.Page', null=True, blank=True)
    
    page_title1 = models.CharField(max_length = 150, null =True, blank=True)
    page_1 = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name="+")
    page_title2 = models.CharField(max_length = 150, null =True, blank=True)
    page_2 = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name="+")
    page_title3 = models.CharField(max_length = 150, null =True, blank=True)
    page_3 = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name="+")
    page_title4 = models.CharField(max_length = 150, null =True, blank=True)
    page_4 = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name="+")
    page_title5 = models.CharField(max_length = 150, null =True, blank=True)
    page_5 = models.ForeignKey('wagtailcore.Page', null=True, blank=True, related_name="+")
    
    
    @property
    def url(self):
        if self.internal_link:
            return self.internal_link.url
        else:
            return self.page_url
       

    def __str__(self):
        return self.menu_text
    
    panels = [
        FieldPanel('page_url'),
        FieldPanel('menu_text'),
        PageChooserPanel('internal_link'),
        MultiFieldPanel([ FieldPanel('page_title1'), PageChooserPanel('page_1'),
                          FieldPanel('page_title2'), PageChooserPanel('page_2'),
                          FieldPanel('page_title3'), PageChooserPanel('page_3'),
                          FieldPanel('page_title4'), PageChooserPanel('page_4'),
                          FieldPanel('page_title5'), PageChooserPanel('page_5')
        ], 
        heading ="Child Item", classname="collapsible collapsed")
    ]
    


class MenuMenuItem(Orderable, menu_item):
    parent = ParentalKey(to='menu.Menu', related_name='menu_items')
    
class MenuManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(menu_name=name)
        
@register_snippet
class Menu(ClusterableModel):
    objects = MenuManager()
    menu_name = models.CharField(null=True, blank=True, max_length=255)
    
    def __str__(self):
        name = self.menu_name
        if not name:
            name = "Unnamed"
            
        return name

Menu.panels= [
    FieldPanel('menu_name'),
    InlinePanel('menu_items', label="Pages"),
    
]
    
