{% load static %}
	{% block awszones %}
		{%for zone in zones%}
		<li>{{ zone }}</li>
		{%endfor%}
	{% endblock awszones %}
