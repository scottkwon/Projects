
    let students = [
    {name: 'Remy', cohort: 'Jan'},
    {name: 'Genevieve', cohort: 'March'},
    {name: 'Chuck', cohort: 'Jan'},
    {name: 'Osmund', cohort: 'June'},
    {name: 'Nikki', cohort: 'June'},
    {name: 'Boris', cohort: 'June'}
    ];

    for(var student in students){
        console.log('Name:'+ students[student]["name"]+ "," + " " + "Cohort:" + students[student]["cohort"])
    }

    let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
       {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
       {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
    };


    for (var user in users){
        console.log("Employees:")
        for(var i in users[user]){
            let num = parseInt(i) + 1
            console.log(num + "-" + users[user][i]['last_name']+ ", " +users[user][i]['first_name'] + "-" + (users[user][i]['first_name'].length+users[user][i]['last_name'].length))
            if(i == 3){
                console.log("Managers:")
            }
        }
    }