# ex10_meteo

<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="" xml:lang="">
<head>
  <meta charset="utf-8" />
  <meta name="generator" content="pandoc" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes" />
  <title>Les données météo</title>
  <style>
    html {
      line-height: 1.5;
      font-family: Georgia, serif;
      font-size: 20px;
      color: #1a1a1a;
      background-color: #fdfdfd;
    }
    body {
      margin: 0 auto;
      max-width: 36em;
      padding-left: 50px;
      padding-right: 50px;
      padding-top: 50px;
      padding-bottom: 50px;
      hyphens: auto;
      word-wrap: break-word;
      text-rendering: optimizeLegibility;
      font-kerning: normal;
    }
    @media (max-width: 600px) {
      body {
        font-size: 0.9em;
        padding: 1em;
      }
    }
    @media print {
      body {
        background-color: transparent;
        color: black;
        font-size: 12pt;
      }
      p, h2, h3 {
        orphans: 3;
        widows: 3;
      }
      h2, h3, h4 {
        page-break-after: avoid;
      }
    }
    p {
      margin: 1em 0;
    }
    a {
      color: #1a1a1a;
    }
    a:visited {
      color: #1a1a1a;
    }
    img {
      max-width: 100%;
    }
    h1, h2, h3, h4, h5, h6 {
      margin-top: 1.4em;
    }
    h5, h6 {
      font-size: 1em;
      font-style: italic;
    }
    h6 {
      font-weight: normal;
    }
    ol, ul {
      padding-left: 1.7em;
      margin-top: 1em;
    }
    li > ol, li > ul {
      margin-top: 0;
    }
    blockquote {
      margin: 1em 0 1em 1.7em;
      padding-left: 1em;
      border-left: 2px solid #e6e6e6;
      color: #606060;
    }
    code {
      font-family: Menlo, Monaco, 'Lucida Console', Consolas, monospace;
      font-size: 85%;
      margin: 0;
    }
    pre {
      margin: 1em 0;
      overflow: auto;
    }
    pre code {
      padding: 0;
      overflow: visible;
    }
    .sourceCode {
     background-color: transparent;
     overflow: visible;
    }
    hr {
      background-color: #1a1a1a;
      border: none;
      height: 1px;
      margin: 1em 0;
    }
    table {
      margin: 1em 0;
      border-collapse: collapse;
      width: 100%;
      overflow-x: auto;
      display: block;
      font-variant-numeric: lining-nums tabular-nums;
    }
    table caption {
      margin-bottom: 0.75em;
    }
    tbody {
      margin-top: 0.5em;
      border-top: 1px solid #1a1a1a;
      border-bottom: 1px solid #1a1a1a;
    }
    th {
      border-top: 1px solid #1a1a1a;
      padding: 0.25em 0.5em 0.25em 0.5em;
    }
    td {
      padding: 0.125em 0.5em 0.25em 0.5em;
    }
    header {
      margin-bottom: 4em;
      text-align: center;
    }
    #TOC li {
      list-style: none;
    }
    #TOC a:not(:hover) {
      text-decoration: none;
    }
    code{white-space: pre-wrap;}
    span.smallcaps{font-variant: small-caps;}
    span.underline{text-decoration: underline;}
    div.column{display: inline-block; vertical-align: top; width: 50%;}
    div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
    ul.task-list{list-style: none;}
  </style>
  <!--[if lt IE 9]>
    <script src="//cdnjs.cloudflare.com/ajax/libs/html5shiv/3.7.3/html5shiv-printshiv.min.js"></script>
  <![endif]-->
</head>
<body>
<header id="title-block-header">
<h1 class="title">Les données météo</h1>
</header>
<nav id="TOC" role="doc-toc">
<ul>
<li><a href="#contexte">Contexte</a></li>
<li><a href="#environnement-de-travail">Environnement de travail</a></li>
<li><a href="#objectifs">Objectifs</a>
<ul>
<li><a href="#lecture-exhaustive">Lecture exhaustive</a></li>
<li><a href="#filtrage-des-données">Filtrage des données</a></li>
</ul></li>
<li><a href="#informations-complémentaires">Informations complémentaires</a></li>
</ul>
</nav>
<style type="text/css">
@import url("https://unpkg.com/sakura.css/css/normalize.css");
@import url("https://unpkg.com/sakura.css/css/sakura.css");
</style>
<h2 id="contexte">Contexte</h2>
<p>Les données stockées dans un fichier texte sont généralement structurées et peuvent être lues et encapsulées dans une liste en utilisant le module <a href="https://docs.python.org/3/library/csv.html">csv</a> comme on l’a vu avec l’exercice <a href="https://perso.esiee.fr/~courivad/python/ex08-meteo.html">Lecture d’un fichier texte structuré</a>.</p>
<p>Cette façon de faire est plus intéressante qu’une méthode naïve car elle évite une étape de traitement. Elle présente cependant l’inconvénient de dissocier la nature des données (stockée généralement dans la première ligne du fichier) et les données elles mêmes.</p>
<p>On va chercher ici à structurer les données dans des dictionnaires.</p>
<h2 id="environnement-de-travail">Environnement de travail</h2>
<p>Pour cet exercice, vous devez utiliser en priorité le fichier squelette <a href="https://perso.esiee.fr/~courivad/python/ex10-meteo.py">ex10-meteo.py</a>. IMPORTANT : Enregistrez le avec <code>Right Click + Save Link As...</code> pour conserver l’encodage.</p>
<p>Selon la convention de structuration des modules, ce fichier sera structuré en quatre parties :</p>
<ol>
<li><strong>Imports et définition des variables globales</strong> ;</li>
<li><strong>Définition des fonctions secondaires</strong> ;</li>
<li><strong>Définition de la fonction principale</strong> ;</li>
<li><strong>Appel protégé de la fonction principale</strong>.</li>
</ol>
<p>Les données sont stockées dans le fichier <a href="https://perso.esiee.fr/~courivad/python/ex08-zip-data-meteo-france-synop.2015110112.csv">ex08-zip-data-meteo-france-synop.2015110112.csv</a></p>
<h2 id="objectifs">Objectifs</h2>
<h3 id="lecture-exhaustive">Lecture exhaustive</h3>
<p>L’objectif est d’écrire une fonction <code>read_data_to_dicts()</code> :</p>
<pre><code>- qui prend en argument un fichier ``csv`` de données météo structurées ;
- et retourne une liste de dictionnaires (un par ligne de données):
    - dont les clés sont les champs de la première ligne du fichier ;
    - et les valeurs les données correspondantes.</code></pre>
<p>Vérifier le bon fonctionnement de la fonction en effectuant un appel depuis <code>main()</code> et en affichant la valeur de retour (les doctests de la fonction donnent des exemples d’appel et les valeurs de retour correspondantes).</p>
<p>Une fois la fonction opérationnelle pour quelques arguments, ET SEULEMENT DANS CE CAS, lancer les doctests dans un terminal.</p>
<h3 id="filtrage-des-données">Filtrage des données</h3>
<p>Le plus souvent seule une partie des données est utilisée pour l’analyse. La fonction <code>read_data_to_dicts()</code> retourne une liste de dictionnaires comprenant l’ensemble des données.</p>
<p>Ecrire une fonction <code>filter_data()</code> :</p>
<pre><code>- qui prend en argument un dictionnaire de données météo du type de ceux retournés par ``read_data_to_dicts()`` ;
- et retourne un dictionnaire simplifié avec uniquement les champs suivants :
    - ``numer_sta`` ;
    - ``date`` ;
    - ``t``.</code></pre>
<p>Vérifier le bon fonctionnement de la fonction en effectuant un appel depuis <code>main()</code> et en affichant la valeur de retour (les doctests de la fonction donnent des exemples d’appel et les valeurs de retour correspondantes).</p>
<p>Une fois la fonction opérationnelle pour quelques arguments, ET SEULEMENT DANS CE CAS, lancer les doctests dans un terminal.</p>
<h2 id="informations-complémentaires">Informations complémentaires</h2>
<p>Le <a href="https://docs.python.org/3/library/csv.html#csv.DictReader">DictReader</a> est une classe adaptée pour stocker les données dans des dictionnaires :</p>
<ul>
<li>en créant un dictionnaire par ligne pour lequel :
<ul>
<li>les clés sont les champs de la première ligne du fichier ;</li>
<li>et les valeurs les données extraites de la ligne</li>
</ul></li>
<li>et en retournant une <em>séquence</em> de ces dictionnaires.</li>
</ul>
<p>Ainsi un fichier comportant :</p>
<ul>
<li>1 ligne de <code>m</code> champs de données ;</li>
<li>et <code>n-1</code> lignes de données (<code>m</code> données par ligne)</li>
</ul>
<p>produira une <em>séquence</em> de <code>n-1</code> dictionnaires comportant chacun <code>m</code> paires clé-valeur.</p>
</body>
</html>
