---
title: Sauvegarde et restauration
summary: Des sauvegardes chiffrées vers un dossier de votre choix, et comment restaurer.
order: 20
---

# Sauvegarde et restauration

Une sauvegarde est un seul fichier chiffré avec tout ce que Damla contient : vos comptes, transactions, plans et réglages. Vous en faites une pour garder vos livres en sécurité, et pour les restaurer si vous supprimez l'app.

## Quand l'utiliser

- Avant de supprimer l'app. Supprimer l'app efface ses données.
- Avant tout grand changement dans vos enregistrements, ou avant d'installer une version de test ou préliminaire de l'app.
- Quand vous voulez une copie que Damla fait chaque jour, sans qu'on le lui demande.
- Quand vous voulez une copie complète de vos livres, conservée hors de l'app et entre vos mains.

Les sauvegardes vivent dans Réglages. Ouvrez Aujourd'hui, appuyez sur l'engrenage en haut à droite, puis sur **Sauvegarde et vos données**. Tout ce qui se trouve sous **Sauvegarde** se passe sur le téléphone ; vous choisissez où chaque fichier est enregistré.

## Pas à pas

### Faire un fichier de sauvegarde

1. Ouvrez Réglages, puis **Sauvegarde et vos données**.
2. Appuyez sur **Exporter une sauvegarde chiffrée**.
3. Tapez une phrase secrète d'au moins 8 caractères et appuyez sur **Exporter**.
4. Appuyez sur le bouton de partage qui apparaît. Enregistrez le fichier dans Files ou iCloud Drive, ou envoyez-le à votre Mac.

> **Careful:** La phrase secrète est la seule clé du fichier. Personne, y compris le développeur de Damla, ne peut ouvrir la sauvegarde sans elle, et Damla ne peut pas la récupérer. Gardez une copie de la phrase en lieu sûr, séparée du fichier.

> **Note:** Restaurer remplace tout sur ce téléphone par la sauvegarde. Vous ne pouvez pas fusionner une sauvegarde avec ce qui existe déjà.

### Restaurer une sauvegarde

1. Ouvrez Réglages, puis **Sauvegarde et vos données**.
2. Appuyez sur **Restaurer depuis une sauvegarde** et choisissez le fichier `damlabackup`.
3. Tapez la phrase secrète de cette sauvegarde.
4. Damla vous avertit que cela remplace toutes les données de ce téléphone. Appuyez sur **Tout remplacer** pour continuer.

Une sauvegarde manuelle et une sauvegarde automatique sont le même genre de fichier, et **Restaurer depuis une sauvegarde** ouvre les deux. La restauration fonctionne depuis n'importe quel fichier de sauvegarde chiffré.

### Laisser Damla sauvegarder toute seule

Les sauvegardes automatiques écrivent le même genre de fichier chiffré dans un dossier que vous choisissez, au plus une fois par jour.

1. Ouvrez Réglages, puis **Sauvegarde et vos données**, puis **Sauvegarde automatique**.
2. Appuyez sur **Choisir un dossier et démarrer** et choisissez un dossier dans le sélecteur Files.
3. Tapez une phrase secrète d'au moins 8 caractères et appuyez sur **Démarrer**. Damla écrit le premier fichier tout de suite.

Dès lors, une copie chiffrée est enregistrée dans ce dossier une fois par jour, quand vous quittez l'app.

> **Note:** La sauvegarde automatique garde sa phrase secrète dans le Keychain de ce téléphone, pour que vous n'ayez pas à la retaper. Vous en avez toujours besoin pour restaurer, gardez donc aussi une copie quelque part hors du téléphone.

L'arrêter avec **Arrêter les sauvegardes automatiques** ne supprime pas les fichiers déjà écrits.

## Bon à savoir

> **Limit:** Une sauvegarde automatique ne s'exécute que lorsque vous quittez l'app. Si vous n'ouvrez pas Damla pendant plusieurs jours, rien n'est sauvegardé pendant ce temps.

- Une sauvegarde que vous exportez à la main reçoit un nom qui commence par `Damla-`, puis la date du jour, et se termine par `.damlabackup`.
- Le nom de fichier d'une sauvegarde automatique commence par `Damla-auto-`, puis la date, et se termine par `.damlabackup`. Le fichier du jour remplace le précédent pour le même jour.
- Un dossier dans iCloud Drive garde aussi la sauvegarde automatique hors de ce téléphone.
- Sur l'écran **Sauvegarde automatique**, vous pouvez voir le dossier et quand la dernière sauvegarde a tourné, et appuyer sur **Sauvegarder maintenant** pour en lancer une tout de suite.
- Les 7 sauvegardes automatiques les plus récentes sont conservées ; les plus anciennes sont supprimées automatiquement.
- Si la dernière sauvegarde automatique a au moins trois jours, Damla montre un rappel sur Aujourd'hui. Si vous n'avez jamais configuré de sauvegarde automatique et que vous enregistrez depuis un moment, Aujourd'hui montre plutôt une ligne « Sauvegardez vos données ».
- Si un essai ou un abonnement a pris fin, Damla devient en lecture seule, mais exporter et restaurer une sauvegarde fonctionnent toujours.
- Si la phrase secrète d'une sauvegarde existante est perdue, le fichier ne peut pas être ouvert. Vérifiez que vous vous en souvenez encore avant de compter sur le fichier.

## Voir aussi

- [Réglages, page par page](/guide/data/settings-map/)
- [Exportation et aperçu famille](/guide/data/export-and-family-snapshot/)
- [Confidentialité et vos données](/guide/data/privacy-and-your-data/)
- [Dépannage](/guide/help/troubleshooting/)
