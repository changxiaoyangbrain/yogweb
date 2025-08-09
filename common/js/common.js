/*
Copyright (c) 2011 TNI. All rights reserved.
Code licensed Creative Commons License:
http://creativecommons.org/licenses/by-nc-nd/2.1/jp/
version:2.0.0
browser:IE6|7|8|9,Firefox,Safari,Chrome,Opera
*/
(function(){
/*@cc_on _d=document;eval('var document=_d'); @*/
var BROWSER={FF:/firefox/i.test(navigator.userAgent),IE09:/msie\s9./i.test(navigator.userAgent),IE08:/msie\s8./i.test(navigator.userAgent),IE07:/msie\s7./i.test(navigator.userAgent),IE06:/msie\s6./i.test(navigator.userAgent),IE:/msie/i.test(navigator.userAgent),SF:/a/.__proto__=="//",OP:/opera/i.test(navigator.userAgent),CH:/chrome/i.test(navigator.userAgent)},PRELOADIMG=[],TAG={a:document.getElementsByTagName("a"),abbr:document.getElementsByTagName("abbr"),address:document.getElementsByTagName("address"),area:document.getElementsByTagName("area"),article:document.getElementsByTagName("article"),aside:document.getElementsByTagName("aside"),audio:document.getElementsByTagName("audio"),b:document.getElementsByTagName("b"),base:document.getElementsByTagName("base"),bdo:document.getElementsByTagName("bdo"),blockquote:document.getElementsByTagName("blockquote"),body:document.getElementsByTagName("body"),br:document.getElementsByTagName("br"),button:document.getElementsByTagName("button"),canvas:document.getElementsByTagName("canvas"),caption:document.getElementsByTagName("caption"),cite:document.getElementsByTagName("cite"),code:document.getElementsByTagName("code"),col:document.getElementsByTagName("col"),colgroup:document.getElementsByTagName("colgroup"),command:document.getElementsByTagName("command"),datalist:document.getElementsByTagName("datalist"),dd:document.getElementsByTagName("dd"),del:document.getElementsByTagName("del"),details:document.getElementsByTagName("details"),dfn:document.getElementsByTagName("dfn"),div:document.getElementsByTagName("div"),dl:document.getElementsByTagName("dl"),dt:document.getElementsByTagName("dt"),em:document.getElementsByTagName("em"),embed:document.getElementsByTagName("embed"),fieldset:document.getElementsByTagName("fieldset"),figcaption:document.getElementsByTagName("figcaption"),figure:document.getElementsByTagName("figure"),footer:document.getElementsByTagName("footer"),form:document.getElementsByTagName("form"),h1:document.getElementsByTagName("h1"),h2:document.getElementsByTagName("h2"),h3:document.getElementsByTagName("h3"),h4:document.getElementsByTagName("h4"),h5:document.getElementsByTagName("h5"),h6:document.getElementsByTagName("h6"),head:document.getElementsByTagName("head"),header:document.getElementsByTagName("header"),hgroup:document.getElementsByTagName("hgroup"),hr:document.getElementsByTagName("hr"),html:document.getElementsByTagName("html"),i:document.getElementsByTagName("i"),iframe:document.getElementsByTagName("iframe"),img:document.getElementsByTagName("img"),input:document.getElementsByTagName("input"),ins:document.getElementsByTagName("ins"),kbd:document.getElementsByTagName("kbd"),keygen:document.getElementsByTagName("keygen"),label:document.getElementsByTagName("label"),legend:document.getElementsByTagName("legend"),li:document.getElementsByTagName("li"),link:document.getElementsByTagName("link"),map:document.getElementsByTagName("map"),mark:document.getElementsByTagName("mark"),menu:document.getElementsByTagName("menu"),meta:document.getElementsByTagName("meta"),meter:document.getElementsByTagName("meter"),nav:document.getElementsByTagName("nav"),noscript:document.getElementsByTagName("noscript"),object:document.getElementsByTagName("object"),ol:document.getElementsByTagName("ol"),optgroup:document.getElementsByTagName("optgroup"),option:document.getElementsByTagName("option"),output:document.getElementsByTagName("output"),p:document.getElementsByTagName("p"),param:document.getElementsByTagName("param"),pre:document.getElementsByTagName("pre"),progress:document.getElementsByTagName("progress"),q:document.getElementsByTagName("q"),rp:document.getElementsByTagName("rp"),rt:document.getElementsByTagName("rt"),ruby:document.getElementsByTagName("ruby"),samp:document.getElementsByTagName("samp"),script:document.getElementsByTagName("script"),section:document.getElementsByTagName("section"),select:document.getElementsByTagName("select"),small:document.getElementsByTagName("small"),source:document.getElementsByTagName("source"),span:document.getElementsByTagName("span"),strong:document.getElementsByTagName("strong"),style:document.getElementsByTagName("style"),sub:document.getElementsByTagName("sub"),summary:document.getElementsByTagName("summary"),sup:document.getElementsByTagName("sup"),table:document.getElementsByTagName("table"),tbody:document.getElementsByTagName("tbody"),td:document.getElementsByTagName("td"),textarea:document.getElementsByTagName("textarea"),tfoot:document.getElementsByTagName("tfoot"),th:document.getElementsByTagName("th"),thead:document.getElementsByTagName("thead"),time:document.getElementsByTagName("time"),title:document.getElementsByTagName("title"),tr:document.getElementsByTagName("tr"),ul:document.getElementsByTagName("ul"),"var":document.getElementsByTagName("var"),video:document.getElementsByTagName("video"),wbr:document.getElementsByTagName("wbr")},GJ=function(){var d=function(b,c,f){switch(b.slice(0,1)){case "#":return document.getElementById(b.slice(1));break;case ".":default:b=b.slice(1);c=c.split(/:/);if(c=="")for(var a in TAG){var d=TAG[a].length;while(d--){var e=TAG[a][d].getAttribute("class")||TAG[a][d].getAttribute("className");e&&e.match(b)||b==""?f(TAG[a][d]):""}}else{var a=c.length;while(a--){var d=TAG[c[a]].length;while(d--){var e=TAG[c[a]][d].getAttribute("class")||TAG[c[a]][d].getAttribute("className");e&&e.match(b)||b==""?f(TAG[c[a]][d]):""}}}}},a={addClass:function(a,b){if(a.className){if(!a.className.match(b))a.className+=" "+b}else a.className+=b},getCSS:function(a){if(!BROWSER.IE)return document.defaultView.getComputedStyle(a,"");else if(a.currentStyle)return a.currentStyle},scanAssociate:function(c,a){for(var b in a)if(a[b])switch(c){case "name":return b;break;case "value":default:return a[b]}},noSpace:function(a){var b=function(b){for(var a=0;a<b.childNodes.length;a++)if(b.childNodes[a].nodeType==1)arguments.callee(b.childNodes[a]);else if(b.childNodes[a].nodeType==3)switch(b.childNodes[a].nodeValue){case "\r":case "\n":case " \r":case " \n":case "\r\n":b.removeChild(b.childNodes[a]);a--}};b(a);a.style.visibility="visible";if(BROWSER.IE06||BROWSER.IE07)a.style.zoom="1"}},c={aHeights:function(c){a.noSpace(c);var d=b.offsetHeight,e=function(c){var k=c.firstChild.className.match("enc0")?parseInt(c.firstChild.className.substr(c.firstChild.className.indexOf("enc0"),5).slice(4)):0,j=0,d=0,g=c.childNodes.length,h=c.childNodes.length;while(g--){while(c.childNodes[g].nodeType!=1)g--;var e=c.childNodes[g],l=k;while(l--)e=e.firstChild;e.style.height="";if(j<e.offsetHeight)j=e.offsetHeight}while(h--){while(c.childNodes[h].nodeType!=1)h--;var f=c.childNodes[h],m=k;while(m--)f=f.firstChild;var b=a.getCSS(f),d=0,i=j;d-=b.paddingTop?b.paddingTop.replace("px",""):0;d-=b.paddingBottom?b.paddingBottom.replace("px",""):0;d-=b.borderTopWidth&&b.borderTopWidth!="medium"?b.borderTopWidth.replace("px",""):0;d-=b.borderBottomWidth&&b.borderBottomWidth!="medium"?b.borderBottomWidth.replace("px",""):0;i+=BROWSER.IE06?i%2==0?d+2:d:d;f.style.height=i+"px"}};e(c);setInterval(function(){if(d!=b.offsetHeight){e(c);d=b.offsetHeight}},250)},clearFix:function(b){if(b.nodeType==1&&b.parentNode.nodeType==1&&!b.parentNode.className.match("clearFix")){var c=a.getCSS(b),d=c?c.styleFloat||c.cssFloat:"";d!="none"&&a.addClass(b.parentNode,"clearFix")}},enclosure:function(a){if(a.className.match(/enc[0-9][0-9]/)){var f=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],d=document.createElement("div"),b=new Number(a.className.substr(a.className.indexOf("enc"),5).slice(3))-1,g,c;d.className="div"+f[0];if(b>25)b=25;g=b;do if(b!=0){var e=document.createElement("div");e.className="div"+f[g-b+1];if(c==undefined){d.appendChild(e);c=d.firstChild}else{c.appendChild(e);c=c.firstChild}if(b==1)while(a.firstChild)c.appendChild(a.firstChild)}else while(a.firstChild)d.appendChild(a.firstChild);while(b--);a.appendChild(d);a.style.visibility="visible"}},distributionBrowser:function(){document.body.setAttribute("id",e)},lateralStripes:function(f){a.noSpace(f);var d=0,e=1,b=f,c={main:function(){while(d<b.childNodes.length){d%2==0?c.odd():c.even();d++}f.style.visibility="visible"},even:function(){a.addClass(b.childNodes[d],"even");e==0?e++:""},odd:function(){a.addClass(b.childNodes[d],"odd");e==1?e--:""}};switch(f.nodeName){case "TABLE":var g=b.childNodes.length;while(g--)if(b.childNodes[g].nodeName=="TBODY"){b=b.childNodes[g];c.main()}break;case "DL":while(d<b.childNodes.length){b.childNodes[d].nodeName=="DT"?e==0?c.even():c.odd():e==1?c.even():c.odd();d++}break;case "OL":case "UL":c.main()}},noSpace:function(b){a.noSpace(b)},nthChild:function(d){a.noSpace(d);var f=2,b=d,c={main:function(){if(b.childNodes.length!=0&&(b.firstChild.nodeType==1||b.lastChild.nodeType==1)){c.first();c.last();d.className.match("nthChild")?c.number(2,1):"";d.style.visibility="visible"}},first:function(){a.addClass(b.firstChild,"first")},number:function(c,d){while(c<b.childNodes.length){a.addClass(b.childNodes[c-d],"num"+c);c++}},last:function(){a.addClass(b.lastChild,"last")}};switch(d.nodeName){case "TABLE":var e=b.childNodes.length;while(e--)if(b.childNodes[e].nodeType==1&&b.childNodes[e].nodeName=="TBODY"){b=b.childNodes[e];c.main()}break;case "DL":d.className.match("nthChild")?c.number(1,0):"";break;default:c.main()}},radius:function(a){var d=document.createElement("span"),e=document.createElement("span"),b=document.createElement("span"),c=document.createElement("span");d.className="partsCTL";e.className="partsCTR";b.className="partsCBL";c.className="partsCBR";a.insertBefore(e,a.firstChild);a.insertBefore(d,a.firstChild);a.appendChild(b);a.appendChild(c);a.style.visibility="visible"},rollOver:function(a){if(!a.className.match("noRoll")&&a.src.match(/_n\./)){var b=PRELOADIMG.length,c=0;while(b--)PRELOADIMG[b].src!=a.src.replace(/_n\./,"_o.")?c++:"";if(PRELOADIMG.length==0||PRELOADIMG.length==c){PRELOADIMG[PRELOADIMG.length]=new Image;PRELOADIMG[PRELOADIMG.length-1].src=a.src.replace(/_n\./,"_o.")}if(BROWSER.IE){a.attachEvent("onmouseover",function(){a.src=a.src.replace(/_n\./,"_o.")});a.attachEvent("onmouseout",function(){a.src=a.src.replace(/_o\./,"_n.")});a.attachEvent("onmouseup",function(){a.src=a.src.replace(/_o\./,"_n.")})}else{a.addEventListener("mouseover",function(){this.src=this.src.replace(/_n\./,"_o.")},false);a.addEventListener("mouseout",function(){this.src=this.src.replace(/_o\./,"_n.")},false);a.addEventListener("mouseup",function(){this.src=this.src.replace(/_o\./,"_n.")},false)}}},toolChip:function(b){switch(b.nodeName){case "AREA":case "INPUT":b.title=b.alt;break;case "DL":case "OL":case "UL":a.noSpace(b);var c=b.childNodes.length;while(c--)b.childNodes[c].title=BROWSER.FF?b.childNodes[c].textContent:b.childNodes[c].innerText;break;default:b.title=BROWSER.FF?b.textContent:b.innerText}}},f=a.scanAssociate("value",BROWSER),e=a.scanAssociate("name",BROWSER),b=document.createElement("div");b.style.visibility="hidden";b.style.position="absolute";b.style.top="0px";b.style.left="0px";b.style.zIndex="0";b.appendChild(document.createTextNode("a"));document.body.appendChild(b);c.distributionBrowser();d(".noSpace","",c.noSpace);d(".lStripes","dl:ol:table:ul",c.lateralStripes);d(".tChip","",c.toolChip);d(".radius","",c.radius);d(".enc","",c.enclosure);d("","",c.clearFix);d("","img:input",c.rollOver);d("","dl:ol:table:ul",c.nthChild);d(".aHeights","div:dl:ol:ul",c.aHeights)};if(BROWSER.IE){var confirm=function(){try{document.body.doScroll("up")}catch(a){setTimeout(arguments.callee,0);return}GJ()};confirm()}else if(BROWSER.OP){var a,confirm=function(){if(document.readyState!="loaded"&&document.readyState!="complete"){setTimeout(arguments.callee,0);return}if(a===undefined){var c=document.getElementsByTagName("link"),d=c.length,b=0;while(d--)b++;if(document.styleSheets.length!=b){setTimeout(arguments.callee,0);return}}GJ()};confirm()}else document.addEventListener&&document.addEventListener("DOMContentLoaded",GJ,false);try{window.addEventListener("load",function(){if(location.hash)location.hash=location.hash},false)}catch(e){window.attachEvent("onload",function(){if(location.hash)location.hash=location.hash})}})()




/* selfFocus
 -------------------------------------------------------- */
var selfFocus={
	load:function(){
		if(self.name==''){
			self.name='meinyu_promotion';
			self.focus();
		}
	},

	event:function(){
		try{window.addEventListener('load',this.load,false);
		}catch(e){window.attachEvent('onload',this.load);}
	}
}
selfFocus.event();




/* openWin
 -------------------------------------------------------- */
function openWin(t,u,n,w,h){
	var a,b=',status=yes,scrollbars=yes,directories=yes,menubar=yes,resizable=yes,toolbar=yes';

	switch(t){
		case 'A':	//何もなし
			a=window.open(u,n,'width='+w+',height='+h+'');
		break;
		case 'popup660':
			a=window.open(u,'popup660','width=675,height=768'+b+'');
		break;
		default:
			a=window.open(u,'popup','width=532,height=451'+b+'');
		break;
	}

	if(a!=null){
		a.focus();
		return false;
	}else{
		return false;
	}
}




/* writeFlash
 -------------------------------------------------------- */
var writeFlash=function(s,w,h){
	var 	a,html='',
				o={
					'classid':'clsid:d27cdb6e-ae6d-11cf-96b8-444553540000',
					'codebase':'http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0'},
				p={
					'allowScriptAccess':'sameDomain',
					'movie':s,
					'quality':'high',
					'wmode':'transparent',
					'menu':'false'},
				e={
					'type':'application/x-shockwave-flash',
					'pluginspage':'http://www.macromedia.com/go/getflashplayer'},
				param=new Array(
				new Array('allowScriptAccess',p.allowScriptAccess),
				new Array('movie',p.movie),
				new Array('quality',p.quality),
				new Array('wmode',p.wmode),
				new Array('menu',p.menu));

	html+='<object classid="'+o.classid+'" codebase="'+o.codebase+'" width="'+w+'" height="'+h+'">';
	for(a=0;a<param.length;a++){html+='<param name="'+param[a][0]+'" value="'+param[a][1]+'">';}
	html+='<embed src="'+s+'" quality="'+p.quality+'" wmode="'+p.wmode+'" width="'+w+'" height="'+h+'" menu="'+p.menu+'" allowScriptAccess="'+p.allowScriptAccess+'" type="'+e.type+'" pluginspage="'+e.pluginspage+'">';
	html+= '</object>';
	document.write(html);
}




/* menu
 -------------------------------------------------------- */
function jsMenu(dir){
	var html='';

	html='<div id="MENU">';
	html+='<p class="logo"><a href="/yogurtlibrary/zh/"><img src="/yogurtlibrary/zh/common/img/logo.png" alt="YOGURT FORUM" width="215" height="133"></a></p>';
	html+='<ul class="lang_menu">';
	html+='<li><a href="/yogurtlibrary/">日本語</a></li><li><a href="/yogurtlibrary/en/">ENG</a></li><li><a class="current" href="/yogurtlibrary/zh/">中文</a></li>';
	html+='</ul>';
	html+='<div class="linkBtnBox">';
	html+='<ul class="tChip">';
	html+='<li class="yogurtoLab">酸奶ラボ</li>';
	html+='<li class="research"><a href="/yogurtlibrary/zh/laboratory/report/">乳酸菌研究最前沿</a></li>';
	html+='<li class="knowledge"><a href="/yogurtlibrary/zh/laboratory/yogurt/">酸奶基础知识</a></li>';
	html+='<li class="researchers"><a href="/yogurtlibrary/zh/laboratory/researcher/">酸奶的研究开发者</a></li>';
	html+='<li class="yogurtoStyle">酸奶スタイル</li>';
	html+='<li class="beauty"><a href="/yogurtlibrary/zh/style/beauty/">酸奶与美容和健康讲座</a></li>';
	html+='<li class="doubt"><a href="/yogurtlibrary/zh/style/dictionary/">释疑解惑！酸奶词典</a></li>';
	html+='<li class="cooking"><a href="/yogurtlibrary/zh/style/science/">科学验证！酸奶与料理的神奇关系</a></li>';
	html+='<li class="choshoku"><a href="/yogurtlibrary/zh/style/choshoku/">从今天开始&quot;肠食&quot;生活</a></li>';
	html+='</ul>';
	html+='<!-- /linkTextBox--></div><!-- /MENU--></div>';
	document.write(html);
}




/* footer
 -------------------------------------------------------- */
function jsFooter(dir){
	var html='';

	html='<!-- フッターエリアここから -->';
	html+='<div id="GlobalFooter">';
	html+='	<div id="footer-inner">';
	html+='		<p class="copyright"><a href="http://www.meiji.co.jp/"><img src="/yogurtlibrary/zh/common/images/globalfooter_logo.gif" border="0" alt="明日をもっとおいしくmeiji 株式会社 明治 Copyright Meiji Co., Ltd. All Rights Reserved." width="181" height="50"></a></p>';
	html+='			<ul class="company-link">';
	html+='				<li><a href="http://www.meiji.com/" target="_blank">明治ホールディングス株式会社</a></li>';
	html+='				<li><a href="http://www.meiji-seika-pharma.co.jp" target="_blank">Meiji Seika ファルマ株式会社</a></li>';
	html+='			</ul>';
	html+='			<ul class="utility-link">';
	html+='				<li class="privacy"><a href="http://www.meiji.co.jp/privacy/">個人情報保護について</a></li>';
	html+='				<li class="rules"><a href="http://www.meiji.co.jp/regulation/">ご利用規約</a></li>';
	html+='			</ul>';
	html+='	</div>';
	html+='</div>';
	document.write(html);
}