{% load static %}
<link rel="stylesheet" type="text/css" href={% static 'index.css' %}>




	{% block vieworder1 %}
		{%for server in Tabs.Provisions.AppServers%}
		<li><a href={{ server }}  class="Provision" target="vieworder"><ul><li><IMG SRC={% static 'logos/'%}{{server}}.jpg ALT="/" id='stuck' height='60' width='60'>{{ server }}</li> </ul></a></li>
		{%endfor%}
	{% endblock vieworder1 %}
