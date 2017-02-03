{% load static %}
<link rel="stylesheet" type="text/css" href={% static 'index.css' %}>




	{% block vieworder %}
		{%for server in Tabs.Provisions.AppServers%}
		<li><a href={{ server }}  class="Provision" target="vieworder"> {{ server }} </a></li>
		{%endfor%}
	{% endblock vieworder %}
