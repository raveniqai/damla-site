---
title: Prix et taux de change
summary: Ce que Damla recherche en ligne, quand, et comment saisir le vôtre.
order: 40
---

# Prix et taux de change

Les données de marché sont la seule recherche que Damla fait de sa propre initiative : les taux de change pour les devises que vous utilisez, et les prix des placements que vous choisissez de suivre. Les deux sont facultatifs, et Damla fonctionne entièrement hors ligne.

## Quand l'utiliser

- Vous avez un compte ou une carte dans une autre devise et voulez que le taux auquel elle est convertie reste à jour.
- Vous suivez une action ou un fonds et voulez que son prix soit récupéré au lieu de le saisir à chaque fois.
- Un taux ou un prix semble faux, et vous voulez voir ce qu'une actualisation a apporté, ou saisir le vôtre pour la journée.

## Ce qui est envoyé, et rien de plus

- Pour les taux, Damla n'envoie que des codes de devise.
- Pour les prix, Damla n'envoie que les symboles boursiers que vous avez définis pour vos placements.
- Aucun montant, nom ou donnée personnelle n'est envoyé. Une recherche de logo par nom de banque, ailleurs dans l'app, ne s'exécute que lorsque vous l'appelez.

## Quand ça s'actualise

- Environ une fois par jour : quand vous ouvrez l'app si les données datent de plus d'un jour, et de nouveau quand vous y revenez après un jour.
- En arrière-plan pendant que l'app est fermée, quand iOS le permet. iOS décide si et quand cela arrive, donc l'actualisation à l'ouverture est celle à laquelle vous fier.
- Chaque fois que vous appuyez sur **Actualiser maintenant** dans Réglages, avec un court délai minimum entre les appuis et un plus long après des échecs.

Chaque source est récupérée indépendamment : si l'une échoue, l'autre garde ses données.

## Pas à pas

### Activer les prix

1. Ouvrez la page du placement et saisissez son symbole boursier. Vous pouvez aussi définir les symboles dans Réglages, **Devises et prix**, sous **Symboles**.
2. Activez **Rechercher les prix des placements** (dans la même page de Réglages, sous **Données de marché**). La recherche de prix est désactivée au départ.

### Vérifier une actualisation, ou saisir votre propre valeur

1. Ouvrez Réglages, puis **Devises et prix**.
2. Appuyez sur **Actualiser maintenant**. Un rapport intitulé **Ce qui a changé** liste chaque source — **Taux de change** et **Prix** — chacune marquée **Mis à jour**, **Ignoré** ou **Échec** :
   - **Mis à jour**, avec une ligne par élément : le nouveau taux ou prix, et ce qu'il était avant (ou *nouveau*, ou *inchangé*).
   - **Ignoré**, avec la raison : la recherche de prix est désactivée, aucun symbole n'est défini, les mises à jour quotidiennes du taux sont désactivées, ou vous n'utilisez que votre devise principale.
   - **Échec**, avec l'erreur. Si un service est occupé, attendez un moment et réessayez.
3. La fin du rapport montre ce que l'actualisation a fait à vos chiffres : la valeur nette et le point le plus bas sur 90 jours, avant et après.
4. Sous **Taux de change**, chaque devise étrangère montre le taux en vigueur et s'il a été **Récupéré** ou s'il s'agit de **Votre taux**, avec sa date. Pour définir votre propre taux, saisissez-le sous **Saisir votre propre taux** et appuyez sur **Enregistrer**.

Sous les interrupteurs, Damla montre quand chaque source a été mise à jour pour la dernière fois, ou **Jamais mis à jour** ; la ligne des prix montre aussi **Désactivé** tant que la recherche de prix est désactivée.

## Quelle valeur l'emporte

- Le taux ou le prix le plus récent est celui en vigueur.
- Un taux ou un prix que vous saisissez l'emporte le jour où vous le saisissez. L'actualisation suivante le remplace par un plus récent récupéré. Le rapport dit quand votre propre valeur est encore utilisée.
- Les prix cotés en pence sont convertis en livres.

## Bon à savoir

> **Note:** Les achats par carte dans une autre devise sont estimés à partir du dernier taux de change plus la majoration de votre banque, 2,5 % quand vous n'en avez pas défini une, et marqués avec ≈ jusqu'à ce que le relevé rende le montant exact. La majoration se définit dans Réglages, **Devises et prix**, sous **Achats par carte dans une autre devise**.

> **Limit:** Une actualisation automatique s'exécute au maximum une fois par jour. Au-delà, n'actualisez que lorsque vous appuyez sur **Actualiser maintenant**. Si le taux ou le prix n'a pas changé après une actualisation, lisez le rapport : il dit ce qui a été mis à jour, ignoré ou a échoué, et si une valeur que vous avez saisie aujourd'hui est encore utilisée.

> **Note:** Les taux viennent de exchangerate-api.com. Les prix viennent d'un service de cotations public.

> **Note:** Damla donne des informations et des estimations tirées de vos propres livres. Il ne donne pas de conseils en investissement ou financiers.

## À lier

- [Placements et investissements](/guide/holdings/investments/)
- [Cartes de crédit](/guide/accounts/credit-cards/)
- [Confidentialité et vos données](/guide/data/privacy-and-your-data/)
- [Dépannage](/guide/help/troubleshooting/)
