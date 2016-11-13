/*$(document).ready(function()
	{
		jQuery.ajax({
            url: "http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&GLOBAL-ID=EBAY-IN&SECURITY-APPNAME=Shoppily-5c49-48fd-b4ab-3334ca087585&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&paginationInput.entriesPerPage=6&keywords=motorola",
            type: "GET",
            dataType:"jsonp",
            success: function(api_data)
            {   
                var json = JSON.parse(JSON.stringify(api_data));
                //json = api data
                for (var i=1;i<3;i++)
                {   $("#ebay").append("<div class=\"row\"></div>");
                    //for(var j=1;j<4;j++)
                    for (var j=1;j<4;j++)
                    {
                        console.log("inside loop 2 "+j);
                        $("#ebay .row").append("<div class=\"col-md-3\"></div>"); 
                        $("#ebay .row .col-md-3").html(
                        "<p> "+json.findItemsByKeywordsResponse[0].searchResult[0].item[j].title[0]+"</p>\
                        <a href="+json.findItemsByKeywordsResponse[0].searchResult[0].item[j].viewItemURL[0]+">"+"<img src="+json.findItemsByKeywordsResponse[0].searchResult[0].item[j].galleryURL[0]+"> </a><br>\
                        Price: "+json.findItemsByKeywordsResponse[0].searchResult[0].item[j].sellingStatus[0].currentPrice[0].__value__+"<br><br>");   
                        console.log("end 2 nd loop "+ (i*j));
                    }
                }
            },
            error : function(jqXHR, textStatus, errorThrown) {
            },

            timeout: 120000,
        });     
	}
);
*/