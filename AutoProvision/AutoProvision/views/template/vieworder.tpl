{% load static %}
<link rel="stylesheet" type="text/css" href={% static 'index.css' %}>




	{% block vieworder %}
		{%for server in Tabs.Provisions.AppServers%}
			<a href={{ server }}  class='Provision' >{{ server }}</a>
			{%endfor%}
	{% endblock vieworder %}