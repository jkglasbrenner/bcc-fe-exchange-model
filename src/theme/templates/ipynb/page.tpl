{%- extends 'basic.tpl' -%}

{% block header %}
<style type="text/css">
div.cell, div.text_cell_render {
  padding: 0;
}

div.input_area > div.highlight {
  margin: 0;
  padding: 0.5em;
}

div.input_area {
  border: thin solid #bfbfbf;
  border-radius: 0;
  background: #f0f0f0;
}

div.input_area, div.output_area {
  margin-bottom: 1rem;
}

div.output_subarea {
  max-width: none;
}

div.output_text {
  border: thin solid #bfbfbf;
  border-radius: 0;
}

div.input_area pre, div.output_area pre {
  margin-bottom: 0!important;
}
</style>
{%- endblock header %}

{% block in_prompt -%}
{%- endblock in_prompt %}

{% block empty_in_prompt -%}
{%- endblock empty_in_prompt %}

{% block output_area_prompt -%}
{%- endblock output_area_prompt %}