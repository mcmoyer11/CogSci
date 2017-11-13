var manualSendResults = "true";

var shuffleSequence = seq("consent","attention_check","test_video", "instructions","trial");

var items = [
    // controller to send results early
        ["sr", "__SendResults__", { }],
    //instructions, consent, attention check, and video test
        ["instructions", "Form", { html: {include: "instructions.html" } } ],
        ["consent", "Form", { html: {include: "consent.html" } } ],
        ["attention_check", "Form", { html: {include: "attention_check.html" } } ],
        ["test_video", "Form", { html: {include: "test_video.html" } } ],
    // trials
        ["trial", "Form", { html: {include: "trial_template.html" } } ],

];

var defaults = [
    // save reaction time for each Form controller
    "Form", {saveReactionTime: "true"}
];
