if(navigator.appVersion.indexOf("Mac",0) != -1){

	if(navigator.appName.charAt(0)=="N"){

		if(navigator.appVersion.charAt(0)==4){

			//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/mac_nn4.css\">");  //Mac Netscape4

		}

		else if(navigator.appVersion.charAt(0)==5){

			//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/mac_nn6.css\">");  //Mac Netscape6

		}

		else {

			//Mac NN3以前　何も処理なし

		}

	}

	else {

		//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/mac_ie.css\">");  //Mac IE

	}

}

else {

	if(navigator.appName.charAt(0)=="N"){

		if(navigator.appVersion.charAt(0)==4){

			//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/win_nn4.css\">");  //Win Netscape4

		}

		else if(navigator.appVersion.charAt(0)==5){

			//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/win_nn6.css\">");  //Win Netscape6

		}

	}

	else {

		//document.write("<link rel=\"stylesheet\" type=\"text/css\" href=\"/yogurtlibrary/zh/css/win_ie.css\">");  //Win IE

	}

}