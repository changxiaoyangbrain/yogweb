function check()
{
	var sel, id, items, age, chk;

	sel = document.getElementsByClassName("nenrei-sentaku")[0];
	id = sel.selectedIndex;
	if (id == 0)
	{
		alert("选择您的年龄");
		return;
	}
	items = document.getElementsByClassName("meneki-check");
	age = sel.options[id].value - 0;
	chk = 0;
	for (var n = 0; n < items.length; n++)
	{
		if (items[n].checked)
			age += items[n].value - 0;
		chk |= ((items[n].checked) ? 1 : 0) << n;
	}
	location.href = "/yogurtlibrary/zh/laboratory/report/1073r1/01/check/result.html?a=" + age + "&c=" + chk;
}