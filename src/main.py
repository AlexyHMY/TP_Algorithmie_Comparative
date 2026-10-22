class Colis:
    def __init__(self, id_colis, poids, valeur, priorite, destination):
        self.id = id_colis
        self.poids = poids
        self.valeur = valeur
        self.priorite = priorite
        self.destination = destination

    def __repr__(self):
        return f"ID: {self.id:<5} | Poids: {self.poids:>3}kg | Val: {self.valeur:>3}€ | Prio: {self.priorite} | Dest: {self.destination}"


class GestionnaireColis:
    def __init__(self):
        self.colis_dict = {}  # Recherche rapide O(1)
        self.colis_list = []  # Pour les parcours et tris O(N log N)
        self.dernier_chargement = []

    def ajouter_colis(self, colis):
        if colis.id in self.colis_dict:
            raise ValueError(f"Un colis avec l'identifiant {colis.id} existe déjà.")
        self.colis_dict[colis.id] = colis
        self.colis_list.append(colis)

    def rechercher_par_id(self, id_colis):
        return self.colis_dict.get(id_colis, None)

    def afficher_tous(self):
        if not self.colis_list:
            print("\nAucun colis enregistré.")
            return
        print("\n--- Liste de tous les colis ---")
        for c in self.colis_list:
            print(c)

    def afficher_tries(self, critere="poids", reverse=False):
        if not self.colis_list:
            print("\nAucun colis enregistré.")
            return
        
        if critere not in ["poids", "valeur", "priorite"]:
            print("Critère invalide.")
            return

        colis_tries = sorted(self.colis_list, key=lambda c: getattr(c, critere), reverse=reverse)
        print(f"\n--- Colis triés par {critere} (Décroissant: {reverse}) ---")
        for c in colis_tries:
            print(c)

    def preparer_camion(self, capacite_max):
        """
        Stratégie gloutonne basée sur un score composite :
        Score = (Valeur * Priorité) / Poids
        """
        if not self.colis_list:
            print("\nAucun colis disponible pour le chargement.")
            self.dernier_chargement = []
            return

        # Calcul du score pour chaque colis (évite la division par 0 si poids = 0)
        colis_scores = []
        for c in self.colis_list:
            poids_effectif = max(c.poids, 0.1)
            score = (c.valeur * c.priorite) / poids_effectif
            colis_scores.append((score, c))

        # Tri par score décroissant
        colis_scores.sort(key=lambda x: x[0], reverse=True)

        chargement = []
        poids_total = 0
        valeur_totale = 0

        for score, c in colis_scores:
            if poids_total + c.poids <= capacite_max:
                chargement.append(c)
                poids_total += c.poids
                valeur_totale += c.valeur

        self.dernier_chargement = chargement
        print(f"\n--- Camion préparé (Capacité max : {capacite_max} kg) ---")
        print(f"Poids total transporté : {poids_total} kg / {capacite_max} kg")
        print(f"Valeur totale transportée : {valeur_totale} €")
        print("Colis sélectionnés :")
        for c in chargement:
            print(f"  -> {c}")

    def afficher_dernier_chargement(self):
        if not self.dernier_chargement:
            print("\nAucun camion n'a encore été préparé.")
            return
        print("\n--- Affichage du dernier chargement ---")
        poids_total = sum(c.poids for c in self.dernier_chargement)
        valeur_totale = sum(c.valeur for c in self.dernier_chargement)
        print(f"Poids total : {poids_total} kg | Valeur totale : {valeur_totale} €")
        for c in self.dernier_chargement:
            print(c)

    def afficher_statistiques(self):
        total = len(self.colis_list)
        if total == 0:
            print("\nAucune statistique disponible (0 colis).")
            return
        
        poids_sum = sum(c.poids for c in self.colis_list)
        valeur_sum = sum(c.valeur for c in self.colis_list)
        prio_moy = sum(c.priorite for c in self.colis_list) / total

        print("\n===== STATISTIQUES DU SYSTÈME =====")
        print(f"Nombre total de colis : {total}")
        print(f"Poids total cumulé    : {poids_sum} kg")
        print(f"Valeur totale cumulée : {valeur_sum} €")
        print(f"Priorité moyenne      : {prio_moy:.2f}")


def main():
    gestionnaire = GestionnaireColis()

    # Initialisation avec les exemples du sujet
    exemples = [
        Colis(101, 8, 20, 2, "Paris"),
        Colis(102, 3, 10, 5, "Lille"),
        Colis(103, 12, 40, 1, "Lyon"),
        Colis(104, 5, 25, 4, "Paris"),
        Colis(105, 2, 15, 3, "Lille")
    ]
    for c in exemples:
        gestionnaire.ajouter_colis(c)

    while True:
        print("\n===== GESTION DES LIVRAISONS =====")
        print("1. Afficher les colis")
        print("2. Ajouter un colis")
        print("3. Rechercher un colis par ID")
        print("4. Organiser les colis (Trier)")
        print("5. Préparer un camion")
        print("6. Afficher le dernier chargement")
        print("7. Afficher les statistiques")
        print("0. Quitter")
        
        choix = input("Choix : ").strip()

        if choix == "1":
            gestionnaire.afficher_tous()

        elif choix == "2":
            try:
                id_c = int(input("ID du colis : "))
                poids = float(input("Poids (kg) : "))
                valeur = float(input("Valeur (€) : "))
                priorite = int(input("Priorité (1-5) : "))
                destination = input("Destination : ").strip()
                
                nouveau = Colis(id_c, poids, valeur, priorite, destination)
                gestionnaire.ajouter_colis(nouveau)
                print("Colis ajouté avec succès !")
            except ValueError as e:
                print(f"Erreur de saisie : {e}")

        elif choix == "3":
            try:
                id_c = int(input("Entrez l'ID du colis à rechercher : "))
                colis = gestionnaire.rechercher_par_id(id_c)
                if colis:
                    print(f"Colis trouvé : {colis}")
                else:
                    print("Aucun colis trouvé avec cet identifiant.")
            except ValueError:
                print("Veuillez entrer un identifiant valide (nombre entier).")

        elif choix == "4":
            print("\nCritères de tri :")
            print("1. Poids")
            print("2. Valeur")
            print("3. Priorité")
            crit_choix = input("Choisissez le critère (1-3) : ").strip()
            rev_choix = input("Ordre décroissant ? (o/n) : ").strip().lower() == 'o'

            mapping = {"1": "poids", "2": "valeur", "3": "priorite"}
            if crit_choix in mapping:
                gestionnaire.afficher_tries(mapping[crit_choix], reverse=rev_choix)
            else:
                print("Critère invalide.")

        elif choix == "5":
            try:
                cap = float(input("Capacité maximale du camion (kg) : "))
                gestionnaire.preparer_camion(cap)
            except ValueError:
                print("Veuillez entrer une capacité valide.")

        elif choix == "6":
            gestionnaire.afficher_dernier_chargement()

        elif choix == "7":
            gestionnaire.afficher_statistiques()

        elif choix == "0":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


if __name__ == "__main__":
    main()