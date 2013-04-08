import datetime
from sqlalchemy import Unicode, Date, DateTime
from sqlalchemy.schema import Column
from camelot.core.orm import Entity
from camelot.admin.entity_admin import EntityAdmin
from timetracker.validators import TrackTimeValidator

class TrackTime( Entity ):

    __tablename__ = 'tracktime'

    track_date = Column( Date(), default=datetime.date.today(), nullable=False)
    start = Column( DateTime(), default=datetime.datetime.now() )
    interval_start = Column( DateTime(), )
    interval_end = Column( DateTime(), )
    end = Column( DateTime(), default=datetime.datetime.now() )
    short_description = Column( Unicode(512) )
    
    def __unicode__( self ):
        return self.track_date or 'Undefined TrackTime data'

    class Admin( EntityAdmin ):
        verbose_name = 'TrackTime'
        list_display = ['track_date', 'start', 'interval_start', 
                        'interval_end', 'end', 'short_description']
        validator = TrackTimeValidator
        search_all_fields = True

