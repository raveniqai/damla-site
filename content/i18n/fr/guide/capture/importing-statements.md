---
title: Importer un relevé
summary: Relevés PDF ou CSV, vérifiés par rapport à vos soldes.
order: 50
---

# Importer un relevé

Importer un relevé bancaire ou de carte fait entrer ses transactions dans votre comptabilité d'un coup, vérifiées par rapport aux soldes que le relevé lui-même indique. Utilisez-le pour démarrer Damla avec un historique, pour rattraper un retard après une coupure, ou pour faire concorder votre comptabilité avec la banque.

## Quand l'utiliser

- Vous configurez l'application et voulez ajouter plusieurs mois d'historique d'un coup.
- Des alertes bancaires sont passées à la trappe certains jours, par exemple sur une carte ou un compte que vous avez commencé à utiliser en cours de mois.
- Vous voulez vérifier votre comptabilité par rapport à la banque : chaque transaction comptée une seule fois, et les soldes qui concordent.

## Pas à pas

1. Ouvrez Comptes, touchez le bouton plus, puis Importer des relevés.
2. Choisissez les fichiers de relevés (PDF ou CSV). Vous pouvez importer plusieurs comptes et plusieurs mois ensemble.
3. Pour chaque fichier, vérifiez ce que Damla a configuré : le nom du compte, s'il s'agit d'un Compte bancaire ou d'une Carte de crédit, et la devise.
4. Activez « Les débits sont imprimés en nombres positifs » si la carte imprime ses débits sans signe moins, et « Les dates sont au format mois/jour (à l’américaine) » si vos dates sont écrites ainsi.
5. Vérifiez ce que Damla a trouvé pour chaque fichier : combien de lignes, s'il correspond à un compte que vous avez déjà, et le solde après la dernière ligne.
6. Si un relevé n'indique pas de solde, saisissez ce que ce compte détient (ou doit, pour une carte) aujourd'hui, pour que le point de départ puisse être calculé.
7. Répondez une seule fois à chaque bénéficiaire inconnu : choisissez une catégorie, marquez-le comme l'un de vos propres comptes, ou ignorez-le. Chaque ligne correspondante suit votre réponse, et la prochaine fois le bénéficiaire est mémorisé.
8. Touchez Importer. Les lignes déjà enregistrées sont ignorées, donc rien n'est compté deux fois, et les lignes en double de fichiers qui se chevauchent sont comptées une seule fois.

> **Tip:** Ouvrez la ligne des lignes ignorées sur l'écran de vérification pour voir comment chacune a été interprétée.

Une ligne arrivée plus tôt comme alerte bancaire compte comme la même transaction quand les montants sont identiques, que les noms de commerces correspondent et que les dates sont à trois jours d'écart au plus. Les banques comptabilisent quelques jours après avoir débité.

## Bon à savoir

- **Tout est lu sur le téléphone. Le relevé n'est jamais téléversé** nulle part : il n'y a ni compte ni serveur.
- **Les PDF verrouillés demandent le mot de passe une seule fois.** Beaucoup de banques verrouillent leurs relevés. Damla demande le mot de passe et peut le garder dans le Keychain de ce téléphone pour que le prochain relevé de la même banque s'ouvre tout seul. Rien n'est synchronisé, et vous pouvez oublier les mots de passe enregistrés dans les Réglages.
- **Les colonnes Débit et Crédit sont lues d'après leur position.** Quand un relevé imprime une colonne Débit et une colonne Crédit, un remboursement et un achat du même montant se ressemblent comme du texte brut. Damla lit donc où chaque nombre était posé sur la page, sous son en-tête de colonne, avant de décider du signe.
- **Quand l'iPhone a Apple Intelligence et que l'encadré récapitulatif d'un relevé de carte est rédigé d'une manière que les règles ne peuvent pas lire**, le modèle sur l'appareil ne lit que cet encadré récapitulatif — ni les lignes de transactions, ni le fichier entier, et rien ne quitte le téléphone. Damla n'accepte rien sur la seule parole du modèle : le code vérifie que chaque chiffre qu'il a renvoyé est imprimé dans le relevé, et que l'arithmétique du récapitulatif lui-même tombe juste, avant que les chiffres ne soient utilisés. Tout chiffre qui échoue à une vérification est écarté, pas corrigé. Rien n'est ajouté tant que vous n'avez pas confirmé l'import. Sur les téléphones sans Apple Intelligence, les lignes de transactions sont quand même lues ; si les soldes du relevé manquent, Damla vous demande plutôt le chiffre du jour.

## Ce qui se passe à la fin

- Si chaque ligne est déjà dans votre comptabilité, le bouton indique Rapprocher du relevé et fait quand même concorder les soldes exactement.
- Si vous n'avez pas enregistré une partie de l'argent une par une, elle est complétée à partir du relevé. Les ajustements de rapprochement antérieurs à l'intérieur de cette période sont remplacés. Au plus deux ajustements clairement libellés sont ajoutés : le report du solde initial et ce qui manque encore à la fin. Les deux sont des lignes de rapprochement, pas des dépenses, et ensuite votre comptabilité correspond aux soldes d'ouverture et de clôture du relevé. Si le relevé n'indique pas de solde de clôture, rien n'est rapproché.
- **Les lignes qui disent quel paiement sur combien elles sont** (marqueurs d'échéances sur un relevé de carte) sont listées sous Échéances trouvées, et rien n'est ajouté tant que vous ne confirmez pas. Elles vont sous la catégorie Échéances, pas comme des dépenses. Les paiements encore à venir sont ajoutés à vos échéanciers aux dates d'échéance ultérieures de la carte.
- Les achats dans une autre devise sont mis à jour au montant que la banque a réellement facturé.

## Articles liés

- [Captures d'écran de votre appli bancaire](/guide/capture/screenshots-of-your-bank-app/)
- [Soldes de départ et ajustements](/guide/accounts/starting-balances/)
- [Bénéficiaires et catégories](/guide/planning/payees-and-categories/)
- [SMS et e-mails de la banque](/guide/capture/bank-texts-and-emails/)
