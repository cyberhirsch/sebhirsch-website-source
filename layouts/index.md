---
title: {{ .Title }}
description: {{ .Description | default .Site.Params.description }}
---

# {{ .Title }}

{{ .Content }}

{{ if .IsHome }}
## Professional Summary
{{ .Site.Params.description }}

## Key Experience
{{ .Site.Params.p1.content | jsonify }}
{{ .Site.Params.p2.content | jsonify }}
{{ end }}
