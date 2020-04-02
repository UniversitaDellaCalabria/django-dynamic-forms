from django.http import HttpResponse

from django_form_builder.forms import BaseDynamicForm
from django_form_builder.models import DynamicFieldMap
from collections import OrderedDict


constructor_dict = OrderedDict([('Telefono',
              ('CustomCharField',
               {'label': 'Telefono',
                'required': True,
                'help_text': 'Fisso o Mobile',
                'pre_text': ''},
               '')),
             ('Credenziali attive dal',
              ('BaseDateField',
               {'label': 'Credenziali attive dal',
                'required': True,
                'help_text': 'Data di attivazione delle credenziali',
                'pre_text': ''},
               '')),
             ('al',
              ('BaseDateField',
               {'label': 'al',
                'required': True,
                'help_text': 'data di scadenza delle credenziali. ATTENZIONE: non saranno considerati valori superiori ai 2 anni.',
                'pre_text': ''},
               '')),
             ('Descrizione Attività',
              ('TextAreaField',
               {'label': 'Descrizione Attività',
                'required': True,
                'help_text': "Descrizione dell'attività per la quale si richiedono le credenziali",
                'pre_text': ''},
               '')),
             ('Richiede che le seguenti anagrafiche vengano attivate',
              ('CustomComplexTableField',
               {'label': 'Richiede che le seguenti anagrafiche vengano attivate',
                'required': True,
                'help_text': 'inserire almeno first_name, last_name e email',
                'pre_text': ''},
               'first_name#last_name#place_of_birth#date_of_birth#codice_fiscale#email#tel#valid_until'))])


def dynform(request):
    form = DynamicFieldMap.get_form(BaseDynamicForm,
                                constructor_dict=constructor_dict,
                                custom_params=None,
                                #data=data,
                                #files=files,
                                remove_filefields=False,
                                remove_datafields=False)

    #context = {'form': form}
    return HttpResponse(form.as_table())
