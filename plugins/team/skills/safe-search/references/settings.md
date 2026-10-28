# Faire tenir la liste dans l'outil

Le skill dit où chercher ; ces réglages font que l'agent ne peut pas aller
ailleurs sans qu'un humain le voie.

Dans le `.claude/settings.json` du projet, un `WebFetch(domain:…)` par domaine
de [sources.md](sources.md) en `allow` : ces pages se lisent sans demander, les
autres domaines restent soumis à confirmation. Ne pas ajouter de règle `ask`
ou `deny` sur `WebFetch` seul : elle passerait avant les `allow` et bloquerait
aussi les domaines autorisés.

```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:docs.python.org)",
      "WebFetch(domain:kubernetes.io)",
      "WebFetch(domain:code.claude.com)"
    ]
  },
  "sandbox": {
    "enabled": true,
    "network": {
      "allowedDomains": ["github.com", "docs.python.org", "kubernetes.io"]
    }
  }
}
```

- `WebFetch(domain:example.com)` ne couvre pas `api.example.com` : ajouter
  `WebFetch(domain:*.example.com)` si besoin.
- La règle `domain:` alimente aussi la liste réseau du sandbox, ce qui couvre
  `curl` et les scripts lancés par l'agent.
- Pour WebSearch, l'outil n'a pas de règle par domaine : le skill passe
  `allowed_domains` à chaque recherche.
