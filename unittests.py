#Unit tests for Flask app

from app import WikiPage, Game, User
import unittest
from pymongo import MongoClient

###STUB mongo DB###

client = MongoClient('localhost', 27017)
db = client['wikiGolf']

preCourses = db.preLoadedCourses
usersDB = db.users


class TestWikiGolf(unittest.TestCase):

	def setUp(self):
		self.WP = WikiPage()
		self.User = User(usersDB) ##not testing user yet
		self.Game = Game(self.WP, self.User)


		"""Tests for WikiPage Class"""

	def testRandomWiki(self):
		"""Tests that a Wikipedia page is succesfully loaded"""
		randomPage = self.WP.loadRandWikiPage()
		self.assertTrue(randomPage)

	def testGivenPagePass(self):
		"""Tests that a specific Wikipedia page is succesfully loaded"""
		givenPage = self.WP.loadGivenWikiPage('Vegetarian_bacon')
		self.assertEqual(givenPage[1], 'Vegetarian bacon')
		self.assertEqual(self.WP.pageCon, baconHTML)

	def testGivenPageFail(self):
		"""Tests that an ambiguos page returns the proper HTML informing
		the user that something has gone wrong"""
		givenPage = self.WP.loadGivenWikiPage('Italian')
		self.assertEqual(givenPage[1], "Unavailable")
		self.assertEqual(self.WP.pageCon, unavailable)

	def testContentWithLinks(self):
		"""Tests to make sure that the html is having all the href's changed for backbone
		and having the right tags left out."""
		pageContent = self.WP.contentWithLinks('Vegetarian_bacon')
		self.assertEqual(pageContent, baconHTML_cleaned)

	"""Tests for Game class"""
	
	def testStartGameRandom(self):
		"""Ensures that the HTML for a random course is added to the courseHTML list
		when method is called"""
		self.Game.startGame(Random = True)
		self.assertTrue(self.Game.courseHTML[0])
		self.assertTrue(self.Game.startPage)
		self.assertTrue(self.Game.endPage)

	def testStartGamenotRandom(self):

		self.Game.startGame(Random = False, par = 3)
		self.assertTrue(self.Game.courseHTML[0])
		self.assertTrue(self.Game.startPage)
		self.assertTrue(self.Game.endPage)

	"""Tests for User class"""
	# in progress

###TEST STRINGS###

baconHTML = """<table class="metadata plainlinks ambox ambox-style ambox-Cleanup" role="presentation"><tr><td class="mbox-image"><div style="width:52px;"><img alt="" src="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/40px-Edit-clear.svg.png" width="40" height="40" srcset="//upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/60px-Edit-clear.svg.png 1.5x, //upload.wikimedia.org/wikipedia/en/thumb/f/f2/Edit-clear.svg/80px-Edit-clear.svg.png 2x" /></div></td><td class="mbox-text"><span class="mbox-text-span">This article <b>may require <a href="/wiki/Wikipedia:Cleanup" title="Wikipedia:Cleanup">cleanup</a> to meet Wikipedia's <a href="/wiki/Wikipedia:Manual_of_Style" title="Wikipedia:Manual of Style">quality standards</a></b>.<span class="hide-when-compact"> No <a href="/wiki/Template:Cleanup/doc" title="Template:Cleanup/doc">cleanup reason</a> has been specified. Please help <a class="external text" href="//en.wikipedia.org/w/index.php?title=Vegetarian_bacon&amp;action=edit">improve this article</a> if you can.</span>  <small><i>(November 2011)</i></small><span class="hide-when-compact"></span></span></td></tr></table><div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Veggie_%22bacon%22_breakfast.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Veggie_%22bacon%22_breakfast.jpg/220px-Veggie_%22bacon%22_breakfast.jpg" width="220" height="198" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Veggie_%22bacon%22_breakfast.jpg/330px-Veggie_%22bacon%22_breakfast.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Veggie_%22bacon%22_breakfast.jpg/440px-Veggie_%22bacon%22_breakfast.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Veggie_%22bacon%22_breakfast.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.23wmf4/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div>Veggie "bacon" breakfast with <a href="/wiki/Bagel" title="Bagel">bagel</a> halves, vegetarian cream cheese, and tomato</div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/wiki/File:Vegan_Bacon_maple_french_toast_cupcakes.jpg" class="image"><img alt="" src="//upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Vegan_Bacon_maple_french_toast_cupcakes.jpg/220px-Vegan_Bacon_maple_french_toast_cupcakes.jpg" width="220" height="165" class="thumbimage" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Vegan_Bacon_maple_french_toast_cupcakes.jpg/330px-Vegan_Bacon_maple_french_toast_cupcakes.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/f/f2/Vegan_Bacon_maple_french_toast_cupcakes.jpg/440px-Vegan_Bacon_maple_french_toast_cupcakes.jpg 2x" /></a>  <div class="thumbcaption"><div class="magnify"><a href="/wiki/File:Vegan_Bacon_maple_french_toast_cupcakes.jpg" class="internal" title="Enlarge"><img src="//bits.wikimedia.org/static-1.23wmf4/skins/common/images/magnify-clip.png" width="15" height="11" alt="" /></a></div><a href="/wiki/Vegan" title="Vegan" class="mw-redirect">Vegan</a> maple "bacon" French toast cupcakes topped with <a href="/wiki/Morningstar_Farms" title="Morningstar Farms">Morningstar Farms</a> Veggie Bacon Strips</div></div></div>
<p><b>Vegetarian bacon</b>, also referred to as <b>fakon</b>, <b>veggie bacon</b>, or <b>vacon</b>, is a product marketed as a bacon alternative, and available in supermarkets. It is high in protein and fiber, yet low in fat, and has no cholesterol. Two slices average 75 calories.<sup id="cite_ref-make_at_home_1-0" class="reference"><a href="#cite_note-make_at_home-1"><span>[</span>1<span>]</span></a></sup> Popular brands include Morningstar and Smart Bacon.<sup id="cite_ref-smart_2-0" class="reference"><a href="#cite_note-smart-2"><span>[</span>2<span>]</span></a></sup> Morningstar Streaky Strips have now been discontinued in the UK.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3"><span>[</span>3<span>]</span></a></sup>
</p><p>Vegetarian bacon is also easy to make at home by marinating strips of <a href="/wiki/Tempeh" title="Tempeh">tempeh</a> or <a href="/wiki/Tofu" title="Tofu">tofu</a> in various spices and then deep frying.<sup id="cite_ref-make_at_home_1-1" class="reference"><a href="#cite_note-make_at_home-1"><span>[</span>1<span>]</span></a></sup> Aficionados of <a href="/wiki/Raw_food" title="Raw food" class="mw-redirect">raw food</a> also use <a href="/w/index.php?title=Coconut_meat&amp;action=edit&amp;redlink=1" class="new" title="Coconut meat (page does not exist)">coconut meat</a> as a bacon subsititute.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4"><span>[</span>4<span>]</span></a></sup>
</p><p>Some commenters have noted that the production of vegetarian products that imitate meat can make life difficult to bring up a vegetarian child.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5"><span>[</span>5<span>]</span></a></sup> In 2008 the animal charity <a href="/wiki/PETA" title="PETA" class="mw-redirect">PETA</a> posted some fake bacon to the actor <a href="/wiki/Daniel_Craig" title="Daniel Craig">Daniel Craig</a>, although it is not known whether he consumed it.<sup id="cite_ref-6" class="reference"><a href="#cite_note-6"><span>[</span>6<span>]</span></a></sup>
</p><p>"Cheeson" The cookbook "American Wholefoods Cuisine: Over 1300 Meatless Recipes from Short Order to Gourmet" includes a bacon substitute that the authors Nikki &amp; David Goldbeck dubbed "Cheeson." They use it in their vegetarian BLT which they dub the "CLT" but it can be used in salads and the like.
</p>
<h2><span class="mw-headline" id="References">References</span><span class="mw-editsection"><span class="mw-editsection-bracket">[</span><a href="/w/index.php?title=Vegetarian_bacon&amp;action=edit&amp;section=1" title="Edit section: References">edit</a><span class="mw-editsection-bracket">]</span></span></h2>
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-make_at_home-1"><span class="mw-cite-backlink">^ <a href="#cite_ref-make_at_home_1-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-make_at_home_1-1"><sup><i><b>b</b></i></sup></a></span> <span class="reference-text"><span class="citation web"><a rel="nofollow" class="external text" href="http://www.bacon.co.uk/Vegetarian_Bacon.htm">"Vegetarian Bacon - bacon.co.uk"</a><span class="reference-accessdate">. Retrieved 18 June 2011</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AVegetarian+bacon&amp;rft.btitle=Vegetarian+Bacon+-+bacon.co.uk&amp;rft.genre=book&amp;rft_id=http%3A%2F%2Fwww.bacon.co.uk%2FVegetarian_Bacon.htm&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-smart-2"><span class="mw-cite-backlink"><b><a href="#cite_ref-smart_2-0">^</a></b></span> <span class="reference-text"><span class="citation web"><a rel="nofollow" class="external text" href="http://www.lightlife.com/product_detail.jsp?p=smartbacon">"Smart Bacon"</a><span class="reference-accessdate">. Retrieved 18 June 2011</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AVegetarian+bacon&amp;rft.btitle=Smart+Bacon&amp;rft.genre=book&amp;rft_id=http%3A%2F%2Fwww.lightlife.com%2Fproduct_detail.jsp%3Fp%3Dsmartbacon&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://www.nspku.org/news/story/morning-star-streaky-strips">http://www.nspku.org/news/story/morning-star-streaky-strips</a></span>
</li>
<li id="cite_note-4"><span class="mw-cite-backlink"><b><a href="#cite_ref-4">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://gothamist.com/2012/09/25/fake_bacon_is_soy_good_try_these_5.php">http://gothamist.com/2012/09/25/fake_bacon_is_soy_good_try_these_5.php</a></span>
</li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b><a href="#cite_ref-5">^</a></b></span> <span class="reference-text">www.alternet.org/story/152091/how_tofurky_and_fake_bacon_actually_glorify_meat-eating</span>
</li>
<li id="cite_note-6"><span class="mw-cite-backlink"><b><a href="#cite_ref-6">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://www.peta.org/b/thepetafiles/archive/2008/11/17/bacon-fake-bacon-for-james-bond.aspx">http://www.peta.org/b/thepetafiles/archive/2008/11/17/bacon-fake-bacon-for-james-bond.aspx</a></span>
</li>
</ol></div>
<p><br />
</p>
<table class="metadata plainlinks stub" style="background: transparent;" role="presentation"><tr>
<td><a href="/wiki/File:Danish_bacon_cooking.jpg" class="image"><img alt="Stub icon" src="//upload.wikimedia.org/wikipedia/commons/thumb/8/84/Danish_bacon_cooking.jpg/40px-Danish_bacon_cooking.jpg" width="40" height="22" srcset="//upload.wikimedia.org/wikipedia/commons/thumb/8/84/Danish_bacon_cooking.jpg/60px-Danish_bacon_cooking.jpg 1.5x, //upload.wikimedia.org/wikipedia/commons/thumb/8/84/Danish_bacon_cooking.jpg/80px-Danish_bacon_cooking.jpg 2x" /></a></td>
<td><i>This <a href="/wiki/Bacon" title="Bacon">bacon</a>-related article  is a <a href="/wiki/Wikipedia:Stub" title="Wikipedia:Stub">stub</a>.  You can help Wikipedia by <a class="external text" href="//en.wikipedia.org/w/index.php?title=Vegetarian_bacon&amp;action=edit">expanding it</a>.</i><div class="noprint plainlinks hlist navbar mini" style="position: absolute; right: 15px; display: none;"><ul><li class="nv-view"><a href="/wiki/Template:Bacon-stub" title="Template:Bacon-stub"><span title="View this template" style="">v</span></a></li><li class="nv-talk"><a href="/wiki/Template_talk:Bacon-stub" title="Template talk:Bacon-stub"><span title="Discuss this template" style="">t</span></a></li><li class="nv-edit"><a class="external text" href="//en.wikipedia.org/w/index.php?title=Template:Bacon-stub&amp;action=edit"><span title="Edit this template" style="">e</span></a></li></ul></div></td>
</tr></table>
"""

baconHTML_cleaned = """<table class="metadata plainlinks ambox ambox-style ambox-Cleanup" role="presentation"><tr><td class="mbox-image"><div style="width:52px;"></div></td><td class="mbox-text"><span class="mbox-text-span">This article <b>may require <a href="/#wiki/Wikipedia:Cleanup" title="Wikipedia:Cleanup">cleanup</a> to meet Wikipedia's <a href="/#wiki/Wikipedia:Manual_of_Style" title="Wikipedia:Manual of Style">quality standards</a></b>.<span class="hide-when-compact"> No <a href="/#wiki/Template:Cleanup/doc" title="Template:Cleanup/doc">cleanup reason</a> has been specified. Please help <a class="external text" href="//en.wikipedia.org/w/index.php?title=Vegetarian_bacon&amp;action=edit">improve this article</a> if you can.</span>  <small><i>(November 2011)</i></small><span class="hide-when-compact"></span></span></td></tr></table><div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/#wiki/File:Veggie_%22bacon%22_breakfast.jpg" class="image"></a>  <div class="thumbcaption"><div class="magnify"><a href="/#wiki/File:Veggie_%22bacon%22_breakfast.jpg" class="internal" title="Enlarge"></a></div>Veggie "bacon" breakfast with <a href="/#wiki/Bagel" title="Bagel">bagel</a> halves, vegetarian cream cheese, and tomato</div></div></div>
<div class="thumb tright"><div class="thumbinner" style="width:222px;"><a href="/#wiki/File:Vegan_Bacon_maple_french_toast_cupcakes.jpg" class="image"></a>  <div class="thumbcaption"><div class="magnify"><a href="/#wiki/File:Vegan_Bacon_maple_french_toast_cupcakes.jpg" class="internal" title="Enlarge"></a></div><a href="/#wiki/Vegan" title="Vegan" class="mw-redirect">Vegan</a> maple "bacon" French toast cupcakes topped with <a href="/#wiki/Morningstar_Farms" title="Morningstar Farms">Morningstar Farms</a> Veggie Bacon Strips</div></div></div>
<p><b>Vegetarian bacon</b>, also referred to as <b>fakon</b>, <b>veggie bacon</b>, or <b>vacon</b>, is a product marketed as a bacon alternative, and available in supermarkets. It is high in protein and fiber, yet low in fat, and has no cholesterol. Two slices average 75 calories.<sup id="cite_ref-make_at_home_1-0" class="reference"><a href="#cite_note-make_at_home-1"><span>[</span>1<span>]</span></a></sup> Popular brands include Morningstar and Smart Bacon.<sup id="cite_ref-smart_2-0" class="reference"><a href="#cite_note-smart-2"><span>[</span>2<span>]</span></a></sup> Morningstar Streaky Strips have now been discontinued in the UK.<sup id="cite_ref-3" class="reference"><a href="#cite_note-3"><span>[</span>3<span>]</span></a></sup>
</p><p>Vegetarian bacon is also easy to make at home by marinating strips of <a href="/#wiki/Tempeh" title="Tempeh">tempeh</a> or <a href="/#wiki/Tofu" title="Tofu">tofu</a> in various spices and then deep frying.<sup id="cite_ref-make_at_home_1-1" class="reference"><a href="#cite_note-make_at_home-1"><span>[</span>1<span>]</span></a></sup> Aficionados of <a href="/#wiki/Raw_food" title="Raw food" class="mw-redirect">raw food</a> also use <a href="/w/index.php?title=Coconut_meat&amp;action=edit&amp;redlink=1" class="new" title="Coconut meat (page does not exist)">coconut meat</a> as a bacon subsititute.<sup id="cite_ref-4" class="reference"><a href="#cite_note-4"><span>[</span>4<span>]</span></a></sup>
</p><p>Some commenters have noted that the production of vegetarian products that imitate meat can make life difficult to bring up a vegetarian child.<sup id="cite_ref-5" class="reference"><a href="#cite_note-5"><span>[</span>5<span>]</span></a></sup> In 2008 the animal charity <a href="/#wiki/PETA" title="PETA" class="mw-redirect">PETA</a> posted some fake bacon to the actor <a href="/#wiki/Daniel_Craig" title="Daniel Craig">Daniel Craig</a>, although it is not known whether he consumed it.<sup id="cite_ref-6" class="reference"><a href="#cite_note-6"><span>[</span>6<span>]</span></a></sup>
</p><p>"Cheeson" The cookbook "American Wholefoods Cuisine: Over 1300 Meatless Recipes from Short Order to Gourmet" includes a bacon substitute that the authors Nikki &amp; David Goldbeck dubbed "Cheeson." They use it in their vegetarian BLT which they dub the "CLT" but it can be used in salads and the like.
</p>
<h2><span class="mw-headline" id="References">References</span></span></h2>
<div class="reflist" style="list-style-type: decimal;">
<ol class="references">
<li id="cite_note-make_at_home-1"><span class="mw-cite-backlink">^ <a href="#cite_ref-make_at_home_1-0"><sup><i><b>a</b></i></sup></a> <a href="#cite_ref-make_at_home_1-1"><sup><i><b>b</b></i></sup></a></span> <span class="reference-text"><span class="citation web"><a rel="nofollow" class="external text" href="http://www.bacon.co.uk/Vegetarian_Bacon.htm">"Vegetarian Bacon - bacon.co.uk"</a><span class="reference-accessdate">. Retrieved 18 June 2011</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AVegetarian+bacon&amp;rft.btitle=Vegetarian+Bacon+-+bacon.co.uk&amp;rft.genre=book&amp;rft_id=http%3A%2F%2Fwww.bacon.co.uk%2FVegetarian_Bacon.htm&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-smart-2"><span class="mw-cite-backlink"><b><a href="#cite_ref-smart_2-0">^</a></b></span> <span class="reference-text"><span class="citation web"><a rel="nofollow" class="external text" href="http://www.lightlife.com/product_detail.jsp?p=smartbacon">"Smart Bacon"</a><span class="reference-accessdate">. Retrieved 18 June 2011</span>.</span><span title="ctx_ver=Z39.88-2004&amp;rfr_id=info%3Asid%2Fen.wikipedia.org%3AVegetarian+bacon&amp;rft.btitle=Smart+Bacon&amp;rft.genre=book&amp;rft_id=http%3A%2F%2Fwww.lightlife.com%2Fproduct_detail.jsp%3Fp%3Dsmartbacon&amp;rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook" class="Z3988"><span style="display:none;">&#160;</span></span></span>
</li>
<li id="cite_note-3"><span class="mw-cite-backlink"><b><a href="#cite_ref-3">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://www.nspku.org/news/story/morning-star-streaky-strips">http://www.nspku.org/news/story/morning-star-streaky-strips</a></span>
</li>
<li id="cite_note-4"><span class="mw-cite-backlink"><b><a href="#cite_ref-4">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://gothamist.com/2012/09/25/fake_bacon_is_soy_good_try_these_5.php">http://gothamist.com/2012/09/25/fake_bacon_is_soy_good_try_these_5.php</a></span>
</li>
<li id="cite_note-5"><span class="mw-cite-backlink"><b><a href="#cite_ref-5">^</a></b></span> <span class="reference-text">www.alternet.org/story/152091/how_tofurky_and_fake_bacon_actually_glorify_meat-eating</span>
</li>
<li id="cite_note-6"><span class="mw-cite-backlink"><b><a href="#cite_ref-6">^</a></b></span> <span class="reference-text"><a rel="nofollow" class="external free" href="http://www.peta.org/b/thepetafiles/archive/2008/11/17/bacon-fake-bacon-for-james-bond.aspx">http://www.peta.org/b/thepetafiles/archive/2008/11/17/bacon-fake-bacon-for-james-bond.aspx</a></span>
</li>
</ol></div>
<p><br />
</p>
<table class="metadata plainlinks stub" style="background: transparent;" role="presentation"><tr>
<td><a href="/#wiki/File:Danish_bacon_cooking.jpg" class="image"></a></td>
<td><i>This <a href="/#wiki/Bacon" title="Bacon">bacon</a>-related article  is a <a href="/#wiki/Wikipedia:Stub" title="Wikipedia:Stub">stub</a>.  You can help Wikipedia by <a class="external text" href="//en.wikipedia.org/w/index.php?title=Vegetarian_bacon&amp;action=edit">expanding it</a>.</i><div class="noprint plainlinks hlist navbar mini" style="position: absolute; right: 15px; display: none;"><ul><li class="nv-view"><a href="/#wiki/Template:Bacon-stub" title="Template:Bacon-stub"><span title="View this template" style="">v</span></a></li><li class="nv-talk"><a href="/#wiki/Template_talk:Bacon-stub" title="Template talk:Bacon-stub"><span title="Discuss this template" style="">t</span></a></li><li class="nv-edit"><a class="external text" href="//en.wikipedia.org/w/index.php?title=Template:Bacon-stub&amp;action=edit"><span title="Edit this template" style="">e</span></a></li></ul></div></td>
</tr></table>
"""

unavailable = "Barnacles! This page is unavailable through the API. Please try <a href='/'> starting over </a>."


if __name__ == '__main__':
    unittest.main()