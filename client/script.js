
function onClickEstimateScore(){
    console.log("Estimate Score button Clicked");
    var venue = $("#venue_ui").val();
    var Innings = document.querySelector( 'input[name="uibtn"]:checked');   
    var ball = $("#ball_ui").val();
    var batting_team = $("#idbatting_team").val();
    var bowling_team = $("#idbowling_team").val();
    var url = "http://127.0.0.1:5000/predict_score_ipl"
    $.post(url,{
        venue : String(venue),
        innings : parseFloat(Innings),
        ball : parseFloat(ball),
        batting_team : batting_team,
        bowling_team : bowling_team
    },function(data,status){
        console.log(data.estimated_score);
        uiestimatescore.innerHTML = "<h2>" + data.estimated_score.toString() + "</h2>";
        console.log(status);
    });
}
function onPageLoad(){
    console.log("loaded");
    var url = "http://127.0.0.1:5000/get_columns";
    console.log("loading")
    $.get(url,function(data, status){
        console.log("got response from get_columns")
        if(data){
            var teams = data.teams;
            var venues = data.venues;
            for(var j in venues){
                var opt = new Option(venues[j]);
                $('#venue_ui').append(opt);
            }
            for(var i in teams){
                if(i<15){
                    var opt = new Option(teams[i]);
                    $('#idbatting_team').append(opt);
                }
                else{
                    var opt = new Option(teams[i]);
                    $('#idbowling_team').append(opt);
                }

            }
        }
    });
}

window.onload = onPageLoad;