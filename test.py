import requests
prompt =  [
    {
        'role': 'user',
        'content': """INSTRUCTIONS :

Vous êtes un assistant en ingénierie logicielle. Vous recevez une spécification textuelle structurée, issue d’un diagramme UML enrichi.

Votre tâche est la suivante :
- Générer uniquement le **corps des méthodes** qui sont accompagnées d’une section **//**.
- Ne pas réécrire les définitions de classes, les signatures de méthodes ou les attributs.
- Le code généré doit être **valide** et conforme à la **syntaxe Java**.

Commencez ci-dessous :
                

public class Chien {

    public Chien() {}
    public void faireDuBruit() {
        // Affiche : "Le chien aboie : Woof!"
    }
}

public class Chat {

    public Chat() {}
    public void faireDuBruit() {
        // Affiche : "Le chat miaule : Miaou!"
    }
}

public class Animal {
    private String nom;
    private int age;

    public Animal() {}
}
"""
    }
]


res = requests.post("https://6101-35-240-254-81.ngrok-free.app/generate", json={"prompt": prompt})
print(res.json())
