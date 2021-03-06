<html>
<head>
    <meta http-equiv="Content-type" content="text/html; charset=iso-8859-1" />
  <link rel  = "stylesheet"
        href = "https://tdt4120.idi.ntnu.no/css/stylesheet.css"
        type = "text/css">
  <!-- MathJax.org -->
  <script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}
  });
  </script>
  <script type="text/javascript" async
    src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
  </script>
  <title>TDT4120 Algoritmer og datastrukturer: Vis kildekode</title>
</head>
<body leftmargin=0 rightmargin=0 topmargin=0 marginwidth=0 marginheight=0>

<!-- old colour=#fe7312 -->

<table width=100% cellpadding=0 cellspacing=0 border=0>
  <tr>
    <td class="container" colspan=2>
      <table width=100% cellpadding=0 cellspacing=0 border=0>
        <tr bgcolor="#eeeeff">
          <td class="container" valign=top><img src="https://tdt4120.idi.ntnu.no/images/heading_left.tdt4120.jpg"></td>
          <td class="container" align=right style="text-align:right" valign=top><img src="https://tdt4120.idi.ntnu.no/images/heading_right.jpg"></td>
        </tr>
      </table>
    </td>
  </tr>

  <tr>
    <td class="container" align=left>
      <img src="https://tdt4120.idi.ntnu.no/images/pixel.gif" width=1 height=15>
      <font color=#888888 face="Tahoma,Arial,Helvetica" size=-2>
      Sist endret: 23.09.2016      </font>
    </td>
    <td class="container" align=right style="text-align: right;">
      <img src="https://tdt4120.idi.ntnu.no/images/pixel.gif" width=1 height=15>
      <font color=#888888 face="Tahoma,Arial,Helvetica" size=-2>
&nbsp      </font>
    </td>
  </tr>
  <tr><td class="container">&nbsp;</td></tr>
  <tr>
    <td class="container" valign=top>
      <table cellpadding=0 cellspacing=0 border=0>
<tr><td class="menu"><img src="https://tdt4120.idi.ntnu.no/images/pixel.gif"
width=13 height=1></td><td class="menu">
<table cellpadding=4 cellspacing=0 border=0>
<tr><td class="menu"><a href="https://tdt4120.idi.ntnu.no/">�vinger</a></td></tr>
<tr><td class="menu"><font size=-3>&nbsp;</font></td></tr>
<tr><td class="menu"><a href="https://tdt4120.idi.ntnu.no/blackboard">Blackboard</a></td></tr>
<tr><td class="menu"><a href="https://tdt4120.idi.ntnu.no/piazza">Piazza</a></td></tr>
<tr><td class="menu"><font size=-3>&nbsp;</font></td></tr>
<tr><td class="menu"><a href="http://www.idi.ntnu.no">IDI</a></td></tr>
<tr><td class="menu"><a href="http://www.ntnu.no">NTNU</a></td></tr>

<tr><td class="menu"><font size=-3>&nbsp;</font></td></tr>
<tr><td class="menu">bendikss logget inn<br />

    <a href="https://tdt4120.idi.ntnu.no/student/oversikt.php">Poengoversikt</a><br />
</table>
</td>
<td class="menu">
<img src="https://tdt4120.idi.ntnu.no/images/pixel.gif"
width=13 height=1>
</td>
</tr></table>
    </td>
    <td class="container" valign=top width=100%>
      <table cellpadding=0 cellspacing=0 border=0 width=100%><tr><td valign=top>

<!-- *****************
       END OF HEADER
     ***************** -->



<h1>Vis kildekode</h1>

<table>
<tr><td>Studentens brukernavn: </td>
    <td>bendikss</td>
</tr>
<tr><td>�ving: </td>
    <td>Kortstokker</td>
</tr>
<tr><td>Fil: </td>
    <td>ov2_main2.py</td>
</tr>
</table>


<p>Leveringsfristen for �vingen er
11.09.2017 15:00</p>


        <table bgcolor=#eeeeff><tr><td><pre>#!/usr/bin/python3

from sys import stdin
from itertools import repeat


def merge(decks):
    result = ''
    while decks:
        min = decks[0][0][0]
        ind, count = 0, 0
        for deck in decks:
            if deck[0][0] &lt; min:
                min = deck[0][0]
                ind = count
            count += 1
        result += decks[ind][0][1]
        if len(decks[ind]) &gt; 1:
            del decks[ind][0]
        else:
            del decks[ind]
    return result


def main():
    # Read input.
    decks = []
    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)
    # Merge the decks and print result.
    print(merge(decks))


if __name__ == &quot;__main__&quot;:
    main()
</pre></td></tr></table>
<!-- ****************
       START FOOTER
     **************** -->

<br><br>
      </td>
      <td><img src="https://tdt4120.idi.ntnu.no/images/pixel.gif"
      width=30 height=1></td>
      </tr></table>
    </td>
  </tr>
</table>
</body>
</html>
