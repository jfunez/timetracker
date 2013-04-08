# -*- coding: utf-8 -*-
from camelot.admin.validator.entity_validator import EntityValidator

class TrackTimeValidator(EntityValidator):

    def objectValidity(self, entity_instance):
        messages = super(TrackTimeValidator,self).objectValidity(entity_instance)
        if entity_instance.interval_end < entity_instance.interval_start:
            messages.append("Interval record must be after of interval start")
        
        if entity_instance.end < entity_instance.start:
            messages.append("Interval record must be after of interval start")

        return messages
