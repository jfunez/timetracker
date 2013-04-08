
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from camelot.admin.action import OpenNewView
from timetracker.model import TrackTime


class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'TimeTracker'
    application_url = 'http://funez.uy'
    help_url = 'http://funez.uy'
    author = 'Juan Fuenz'
    domain = 'funez.uy'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        return [ Section( _('Tracked Times'),
                          self,
                          Icon('tango/22x22/actions/appointment-new.png'),
                          items = [TrackTime] ),
                 Section( _('Configuration'),
                          self,
                          Icon('tango/22x22/categories/preferences-system.png'),
                          items = [Memento, Translation] )
                ]
    
    def get_actions(self):
        new_timetrack_action = OpenNewView( self.get_related_admin(TrackTime) )
        new_timetrack_action.icon = Icon('tango/32x32/actions/appointment-new.png')

        return [new_timetrack_action]