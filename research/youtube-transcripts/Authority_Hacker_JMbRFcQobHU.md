# Transcript

**Expert:** Authority_Hacker

**Video ID:** JMbRFcQobHU

**Collected:** 2026-06-25 07:20:11

---

[0.08] Today, we're lifting the curtain on how
[2.08] a real business actually uses AI behind
[5.04] the scenes. Not the flashy social media
[7.36] post that everyone makes, but the boring
[9.92] internal work that saves us hours and
[12.16] brings in lots of revenue, like our
[14.72] support bot that answers members
[16.56] questions while we sleep, a database
[18.88] that flags which customers are about to
[21.12] cancel, and a course that Claude Code
[23.6] built in just 45 minutes. I'm joined by
[26.0] Gail Breton, my co-founder, Authority
[27.76] Hacker, where we show you what actually
[29.76] works for business owners, not what
[32.08] looks good on camera. Let's jump right
[34.16] in. And really, the goal of this
[35.92] episode, Mark, is just to show people in
[38.0] real life how we use vibe coding to run
[41.68] a business that is mostly information
[43.68] work that you know, operations that are
[45.84] not necessarily what people do, but
[47.2] rather things they can get inspired from
[49.76] that could help them in their daily
[51.2] operations. And you'll see that most of
[52.56] this is non-custofacing. And yeah, let's
[54.64] just jump on the first one.
[55.68] >> Okay, so uh I'm going to go first. One
[57.92] of the things which we offer in our
[61.68] product in the plus tier is a WhatsApp
[64.0] community. And it's literally just a
[65.68] WhatsApp chat group that I've set up.
[68.32] It's none of the we don't have any of
[69.6] the business infrastructure set up. It's
[71.12] just like me personally on my phone set
[73.84] that up. And I need to make sure that
[76.24] the hund and something people who are
[78.8] trying to join that a are entitled to
[82.16] like they have the right membership
[83.52] access to be able to do that. I need to
[85.52] make sure I have their phone numbers. I
[86.96] need to make sure I add them to WhatsApp
[88.72] and that I've track in our system in
[91.28] circle uh our memberships software that
[94.16] they have been added so I don't try and
[96.24] do that again or anything and I know if
[98.0] I need to remove people in future that
[99.6] that's easy to keep track of as well.
[101.68] So, it's a really simple process that I
[104.32] was just doing it manually in the
[105.6] beginning cuz it's like ah, it takes 2
[107.36] minutes. Like, doesn't matter. But, it's
[109.36] one of these things that just the more
[110.72] it comes up, the more you do it, it's
[112.4] like, ah, this is a pain. This is a
[113.68] pain. I wish I'd automated this sooner
[115.52] and kind of bought back some of this
[116.88] time. Uh, so I'm just going to show you
[118.64] the automation in practice. All I do
[121.28] load up Cloud Code. And if you type/W
[124.56] WhatsApp on boarding, it's going to load
[126.32] my WhatsApp on boarding skill. It's
[129.04] going to pull the data from the
[131.28] application sheet which it's set up and
[134.24] it's going to give me the phone number
[135.84] of the person I need to or the people I
[138.24] need to add to WhatsApp. I copy that, I
[140.72] go over to WhatsApp and I paste that in
[143.04] and add them. That bit is manual, but
[145.12] the rest, all the logging, all the
[147.12] templating is automated. And I've just
[150.32] now also set that up as a routine, which
[153.36] is a triggered workflow. So every day at
[156.8] 6:00 a.m. now, this workflow is going to
[160.48] run and it's going to do it. So I don't
[162.72] have to even like think of doing it
[164.16] manually. It's just automatically going
[165.68] to happen.
[166.08] >> The one thing you need to watch out with
[167.36] routines is the threats don't show up on
[169.6] your chat history on the left. They show
[171.44] up in that routine and on your phone
[173.44] only.
[173.84] >> Yeah.
[174.16] >> So yeah, and it's good 6 a.m. because it
[176.0] starts your limits early as well, which
[177.28] means you get a shorter session on your
[178.8] first session, which means you can
[179.92] hammer close code when you wake up. All
[181.6] right, so let's talk about how this
[183.36] actually works in practice. And this is
[186.72] the unfiltered reality of how we set it
[189.2] up. And I just want to say now, it's not
[191.12] perfect. So Gail, I know you're like
[194.32] here [snorts] shaking your head in
[196.08] disgust that why I still have Zap here,
[198.16] but I'll explain that as I'm going
[199.36] through it. So we have a form which is
[202.8] embedded in our circle community in a
[205.28] space that only plus members and max
[207.12] members have access to and they update
[210.24] their profile field basically and when
[212.8] they do that Zapier is listening out and
[215.84] it triggers an automation which sends me
[218.08] a Slack notification and it adds that
[220.24] data to Google sheet 100% we can
[223.6] automate this with cloud code like we
[225.76] don't need Zapier for it at all
[227.76] >> when I set it up we have have a Zapier
[229.92] account. We're using it for some other
[231.36] stuff. I was like, this is the lowest
[232.88] friction way to do this right now. I
[234.48] just I just need to need this set up.
[236.16] This was before I built the skill. By
[237.84] the way, uh this was just to trigger
[239.6] notifications. So, it gets added to a
[241.76] Google sheet, and I used to just have to
[243.92] go in, check that Google sheet, update
[245.68] it manually, check if they had the right
[247.36] access, do all that stuff. Now, however,
[250.48] when that skill runs, it has access to
[252.88] my Google Drive through the Google Drive
[256.16] CLI, which is like a sort of MCP thing.
[258.8] It's basically has full access to read
[260.32] and write everything. It was a bit of a
[261.68] pain in the ass to set up, but you know,
[263.68] Claude Code walked me through it. And
[265.2] once you have that set up, you can read
[266.8] and write things. I think my mistake
[268.88] early on was I thought I could use the
[271.2] clawed connector in there to do
[273.76] everything, but apparently that can only
[275.28] read information.
[276.16] >> It doesn't have a right title,
[277.12] >> not write [snorts] to it. So that was
[279.28] that was a bit of a Yeah.
[280.96] >> For the members who are listening, I
[282.32] actually made a lesson on connecting
[283.76] this specific CLA in a new course. And
[286.56] so it's like I teach CLA in general, but
[288.72] I use that one because I know it's a
[290.08] handy one. So it's like there's
[291.84] >> all it is, all a CLI is really is a way
[294.64] for AI in this case, so cloud code to
[298.32] access all of the functions that are
[301.52] possible inside Google Workspace, right?
[304.0] So it can open a sheet, it can read a
[306.08] sheet, it can write to a cell, that kind
[308.08] of thing. And it just makes it very
[309.44] streamlined and very easy and very quick
[311.28] for it to do. So you can also achieve
[313.04] the same thing using the MCP as well. So
[316.48] next thing is Claude will read the sheet
[318.96] and it looks up the members circle ID.
[322.0] So that's the data we get out of circle
[324.72] and I think out of Zapier as well. It's
[326.32] like this ID. It doesn't mean anything
[327.84] to me. I have to use AI to look it up
[330.56] but it does automatically. It figures
[332.96] out what membership tier they're in and
[335.2] if they are in the right membership tier
[337.28] then it's going to add it to my list of
[339.2] people to add and I just copy it. Gives
[342.88] me everything in a copy pasteable
[344.24] format. I add them to WhatsApp. They're
[346.64] in WhatsApp. I type done and then Claude
[349.84] tags everyone correctly so we know who's
[352.08] who's in there. Updates the member
[353.6] fields. Very very very simple
[356.24] automation. And as you can see like
[358.56] Claude does all these like really minor
[361.28] things like you know checks there's no
[363.12] duplicates so nobody's added twice. you
[366.08] know, it makes sure they have the right
[367.52] membership tier. Make sure like all the
[369.84] data in circles uh added and it's like
[372.56] uh it's very easy for me to copy paste
[374.16] in uh because it has like the plus
[375.84] symbol for international phone numbers
[377.92] cuz like sometimes people don't have
[379.28] that. It's like it just fixes all the
[381.68] tiny stuff that takes me like a few
[383.76] seconds or a minute here or there. But
[385.84] that really adds up over time.
[387.6] >> Here's my question. that
[388.96] >> why don't you try to use the computer
[391.2] use to have it add people on the
[392.88] WhatsApp app if it runs like 6 a.m.
[395.92] >> Yeah. I mean it's probably the next
[397.2] thing I could do with it. Uh I mean the
[398.8] honest answer is when I last used
[400.8] computer use admittedly this was like 4
[402.72] months ago or something. It was pretty
[405.12] crap. But I I hear it's gotten a lot
[407.2] better. So yeah.
[408.4] >> And it's not just that. It's like you
[410.0] have time right 6 a.m. You're probably
[411.36] not at your computer at the time. So
[412.72] even if it's slow as hell like you can
[415.04] probably just do it. I do more and more
[417.44] browser use, computer use now actually.
[419.28] It's not perfect. It's slower and it's
[421.2] clunky but it will do it eventually if
[423.68] you give it enough time basically. So
[425.28] yeah, I mean that's like very simple
[426.72] basic skill. I think anyone can build
[428.32] that in a very short space of time. You
[431.2] though have created a slightly more
[433.68] complex skill and then done something
[435.92] quite different with that. So that's
[438.24] probably like the next level up from
[440.4] just building a simple skill. You want
[442.08] to talk to us about that now?
[443.44] >> Yeah. So I mean as we said we're going
[445.2] gradually more complex through this.
[447.2] Your first one was like a simple scale.
[448.8] The next one I have is actually still
[450.48] kind of a scale and the output is
[453.12] basically like the lesson notes. So for
[455.68] example this is the new course that we
[457.6] just released like the clo code means
[458.96] business one which is an update to our
[460.8] code course but it has like new work
[462.8] templates works a little bit like open
[465.44] and her and stuff but the point is the
[467.44] entire course inside circle which is the
[469.44] platform that we use was created by
[471.04] cloud code. The only thing I did was
[472.96] shoot the videos and they were edited
[474.64] through the script and then I basically
[477.76] gave clude code the link to the videos
[479.76] on the script and it did everything. It
[481.76] created the lesson notes. It created the
[484.08] illustrations. It humanized the whole
[486.4] thing. So you won't see a single m dash
[488.08] here and it actually sounds pretty good
[489.92] and sounds like me. Did all that. Uh and
[492.64] it didn't create one lesson. It created
[494.8] all lessons, all notes, everything when
[497.52] the course is done in one prompt
[499.76] basically. And I can actually show you
[501.2] the prompt. You can see the prompt that
[503.28] I uh actually gave it was like hey I
[505.76] want to create a new course called cloud
[506.96] coin business and circle not published
[508.88] yet. Uh create the lessons video 1 to9
[511.84] including 2.5. It's like a lesson I put
[513.68] in between and I just I did not even
[515.6] export the videos or the transcripts or
[517.36] anything. I just gave it the link to the
[519.28] folder on the script which is like the
[521.28] you know cloud video editing tool that
[522.8] we're using. And I was like, for each
[524.48] video I want you to create beginner
[525.84] friendly non-jargony lesson notes that
[527.52] walk them through the step and the
[528.88] concept and what to do well formatted.
[531.44] When explaining concept, create images
[532.96] using GPT images, which is another skill
[535.2] that we have, like the image that you
[536.48] just showed, for example, just basically
[538.24] did that. And I just told it like
[539.92] whiteboard plus handdrawn marker, which
[541.52] is kind of the style I usually go for.
[543.04] And I kind of keep it consistent. For
[545.28] each lesson, create a thumbnail with my
[546.96] photo. And so again, for all the
[548.96] thumbnails of all the videos were also
[550.64] created in one shot. So that means 10
[552.16] thumbnails plus about 30 to 40 images
[554.88] plus about 10 lesson notes. And I said,
[556.88] "When you're done, upload everything on
[558.16] Circle. Point me to the folder with the
[559.52] thumbnails cuz the thumbnails I need to
[560.88] upload with the videos at the end. Ask
[562.64] me any question if you need more
[563.84] context. You can see the outline of the
[565.36] course here." And I gave it a notion
[567.28] link. Like again, I did not export
[568.8] anything or whatever. It's just all
[570.0] connected to everything. And Godspeed.
[572.0] >> I uh [laughter] I like how you wrote
[573.68] Godspeed at the end. Does that think
[576.0] that made any difference?
[577.2] >> No. Uh it's just fun for me. So this is
[580.0] like a really complex project. Not a
[582.72] task, it's a project. I mean when we had
[584.96] a team of people before this was, you
[587.2] know, like multiple people working on
[588.96] this for, you know, days if if not a
[591.52] week
[592.16] >> to pull something like this together. So
[593.84] it's pretty impressive you're able to do
[595.52] that with just this one prompt. Now
[597.28] >> this was about basically because the
[599.92] model is like clawed code and the model
[601.92] is so good now or what's the reason it's
[603.52] able to pull this off? Yeah, it's just
[605.68] able to kind of like stay on track
[607.28] longer and I think that's kind of what
[608.8] you see in terms of the models getting
[610.72] better. So a lot of people are like ah
[612.16] Opus 4.8 is it really better than Opus
[614.32] 4.5 etc. It is but not necessarily like
[617.44] early in the context of for small tasks.
[619.44] It's like the way I explain to people is
[620.8] like you cannot write emails 10 times
[623.44] better anymore with AI. Like there's no
[626.0] way to write better.
[627.04] >> Diminishing returns on what you can get.
[629.36] And especially if you watch, you know,
[631.2] we're guilty of this as well, like
[632.56] YouTube videos, podcasts, uh where
[634.56] people are talking about the new models
[636.0] like they come out and they have a few
[638.8] hours or minutes to test it. So they go
[640.8] like, oh, generate an image or write an
[642.4] email or do all the stuff they've done
[643.76] before. But it there's marginal
[646.08] difference versus like a big project
[647.84] like this with thought uh you know it
[650.08] takes like a lot longer to actually
[652.4] produce it. So that's where you're
[653.68] seeing the difference. So
[654.64] >> yeah it's like these outputs are
[655.84] saturated basically at this point like
[657.12] they will get marginally better with the
[658.56] new models and like you'll find a slight
[660.16] improvement but the reality is like this
[661.76] is where we've progressed in the last
[663.2] six months is like you need to be more
[664.96] ambitious with your prompts and give
[666.24] them bigger things. It's a discussion we
[667.84] have a lot internally is like how can we
[669.44] just offload more responsibility. This
[671.28] was literally like this is going to be
[672.48] studentf facing and you're building
[674.4] this. Now the two things that I had to
[676.4] do that was uploading the videos and the
[678.72] thumbnails mostly because the MCP
[680.16] doesn't allow not because clo couldn't
[681.6] do it. It's just like it doesn't have
[683.6] >> circle MCP doesn't allow uh yeah
[686.4] uploading videos. Okay, that makes
[687.6] sense.
[688.08] >> And then other than that it was adding
[690.32] some screenshots. So like taking
[692.4] screenshots for some areas. So for
[693.92] example the initial install. You can see
[695.68] the thumbnails are good by the way.
[696.8] They're not too bad basically. And like
[698.64] these screenshots for example I did
[699.92] manually because we're not at the point
[702.08] where it's good enough to create the
[703.52] right screenshots at the right place
[705.04] etc. So I created a few screenshots. You
[706.88] can see otherwise the explainer images
[708.56] etc. They're good. They're like simple
[710.16] for beginners. Uh yeah it's very
[712.8] scannable. It did the formatting very
[714.4] well. It did all of that. It figured it
[715.92] all out for me basically. And so in the
[717.6] end putting this whole course together
[719.04] was like code walking for 45 minutes and
[721.04] me maybe another 45 minutes of like
[723.6] making sure that screenshots are here,
[724.96] uploading the videos and uploading the
[726.56] thumbnails basically. And there's about
[728.08] 10 lessons. There's 10 more that are
[729.44] coming out actually uh this week. So
[731.6] this course will be at 20 lessons. But
[733.28] the idea is like yeah, I just need to
[735.2] shoot videos now. And then everything
[737.04] else is almost fully automated and it's
[740.32] quality like I don't think the quality
[742.0] compared to what we used to do
[743.28] previously. I don't think the quality
[744.96] has dropped. Arguably it's better like
[747.44] the explainer images etc. We didn't do
[749.28] that before. So that shows you as well
[751.04] how you can combine multiple skills
[752.56] because there's a skill for creating the
[753.68] lesson nodes. There's a skill for
[754.96] creating images. There is like some
[756.72] skills that explain how to use circle
[758.4] for example. It kind of combines all
[759.84] these things into one mega prompt and
[761.52] does that.
[762.08] >> Something I want to add here because you
[763.76] know a lot of people challenge us on
[766.16] like hey you know when I use AI it's it
[768.72] just gives me kind of slop it's not as
[770.32] good but I think the difference here is
[772.8] that you have created original content
[775.04] here in the tutorial
[776.4] >> the video. Yeah right exactly the video.
[778.16] >> So it's not like making up facts about
[780.96] how to get cloud code up and running
[783.2] itself. It's using your information and
[786.0] it's just like finding nicer or clear
[788.96] ways to articulate points that you've
[791.36] already made. So, it's really like a
[793.12] repurposing task rather than a full
[796.24] generation task here. That's why it
[798.08] sounds
[798.48] >> does it has a bit of freedom in the
[800.0] sense that it's allowed to expand a
[801.52] little bit what I say. So, you can go
[802.88] and use web search and it's like let's
[804.64] say there's like some details, some
[805.92] settings that I forgot to mention,
[807.28] whatever. It will kind of correct me in
[809.44] the le notes and then make sure the
[811.92] whole thing is better. But like, you
[813.12] know, it's like a little bit of wiggle
[814.32] room, not like start from scratch. And I
[816.72] did the planning. I did all of that. I
[818.08] used AI to help me with the planning.
[819.6] Sure. But it's like I was involved and
[822.0] it wasn't like fully automated,
[823.52] whatever. What was fully automated was
[824.96] like all the boring work basically like
[827.36] all the rewriting things and making sure
[829.12] the notes are clear, uh, making these
[830.96] explainer images, briefing them, all of
[833.04] that, like the prompting. I didn't have
[834.4] to download them. I didn't have to do
[835.6] anything. It just uploaded them for me.
[837.52] Like all that busy work. And I think
[839.52] that's kind of the thing. It's like
[840.64] people aim to make AI create their
[842.96] content. But I think they should free up
[844.88] their time to create content uh exactly
[847.68] and then just have AI do all the boring
[849.6] stuff uploading all the even editing
[851.84] etc. And then that's how you create
[853.6] content that people still care about. So
[855.12] this course is quality like people love
[856.8] it so far. We've had really good
[858.24] feedback.
[859.44] >> I think as well people are so people
[863.04] might be watching this and think oh I'm
[864.72] not creating courses or I'm not so much
[866.56] of a content creator. This doesn't apply
[868.08] to me. But let's say you know you're an
[869.76] agency or you're in an internal sort of
[872.08] B2B team right you are creating content
[875.6] when you have calls with your clients or
[877.44] sales calls or any kind of call that you
[879.76] have a transcript with you can run a
[881.76] similar process here to you know
[883.76] generate your proposals or
[886.16] >> um your project plans or whatever else
[888.4] it might be and it'll like it's not
[890.96] difficult to build something like that.
[892.4] I mean you saw Gail's prompt there as
[894.08] well like three or four paragraphs
[895.52] >> because there's a lot of skills behind
[896.64] but yeah sure like once you've built
[898.08] your infrastructure like you need to
[899.76] kind of build this kind of knowledge
[900.88] base same like my workspace has a lot of
[903.04] knowledge about the company the tone
[904.64] everything like it has a lot of context
[906.48] to use and that's why like I think it
[908.88] reads well like I think it's like the
[910.4] reading the writing for example is very
[912.32] clear and it doesn't feel like it was
[914.8] like super badly written by AI for
[916.64] example um because you have that context
[919.04] >> and I'm just going to take a sec to do a
[920.4] shameless plug here but if you want to
[921.76] learn how to build a workspace exactly
[923.6] like that and all the skills that go
[925.36] behind that. Then we're actually running
[926.64] a free webinar for you guys next
[929.44] Tuesday. That's going to be the 16th of
[931.04] June. It's at 5:00 p.m. UK time, so it's
[933.28] about noon Eastern time. Uh it's
[935.92] completely free. Gail and I'll be
[937.2] hosting it and we're going to show you
[938.16] behind the scenes on how we build all
[940.32] this kind of stuff, how we set up our
[941.68] Claude Code workspace. And it is for
[944.24] business owners who are non-technical.
[946.4] So don't worry if you've never written a
[948.24] line of code in your life. We don't
[950.24] write code. We communicate with claude
[951.92] code in English. Uh, and you can build
[954.0] all this stuff pretty quickly. Y
[956.32] >> um, and we'll show you how to do stuff.
[957.84] >> We're going to show you some better
[958.96] ones. These are the easy things. This is
[960.48] the lowest level basically [laughter]
[962.56] >> like day one or week one stuff. Yeah.
[964.96] >> Yeah. This is so
[965.92] authorityhacker.com/webinar
[968.48] and you can sign up for free there. Hope
[970.56] to see you there. All right, Gail. So,
[972.64] we've talked about making simple skills.
[975.12] We talked about making some more
[976.4] advanced skills, but something we've
[979.12] been doing a little bit more of is
[980.64] taking skills and turning them into kind
[983.76] of autonomous agents or bots or what
[986.8] would you really call these things?
[988.08] Yeah. I mean, basically moving them like
[990.0] these things, they run on your clothes
[991.44] code. You're usually typing on your
[992.96] keyboard for these things to happen.
[994.32] It's like how do you make them happen
[995.76] when you're not at your keyboard? And I
[997.92] think you wrap a bit more code around it
[999.84] and you host it on the cloud basically.
[1002.0] Like how do you do that? And I think
[1003.52] that's kind of the logic like
[1005.28] progression. You start with like making
[1006.96] a skill. You're like, am I happy with
[1008.64] this? Is AI doing a good job? Etc. And
[1010.8] then for some jobs, for the courses, I
[1012.72] wouldn't do that. But like for some of
[1014.16] the jobs we're going to show you, it
[1015.44] makes sense that you should not even be
[1017.68] intervening at all and it just happens.
[1019.84] And then that's kind of like you build
[1021.6] this for the multiplayer when your
[1023.76] attention is not even needed for the
[1025.44] thing to happen because that's kind of
[1026.96] the limitation that we are starting to
[1028.32] feel right now. It's like we run all of
[1029.52] these things on code etc. But you're
[1031.52] kind of running like five threads at
[1033.04] once and so on and there's a lot of
[1034.56] things happening and then it's like
[1035.92] you're still
[1036.4] >> it's not it's not even like that's not
[1038.4] the problem that you're running five
[1039.68] physical threads in claw code. It can
[1041.44] handle that. It's your like it's your
[1043.76] brain.
[1044.08] >> My brain is the bottleneck. Yeah. Cuz
[1046.16] like you do five times as much work and
[1048.96] that's great, but then you have to think
[1050.4] about five times as many things. And
[1051.92] even though you're not physically doing
[1053.36] it, it's like you're doing less actions
[1055.6] like actions per minute but like your
[1057.68] thoughts per minute is like way way
[1059.92] higher. And that is tiring.
[1061.68] >> Yep.
[1062.08] >> Uh so this kind of gets around that.
[1063.84] >> Okay. So the next part I want to show
[1065.6] you is actually our support bot. So it's
[1067.68] actually we have a get help section and
[1070.64] you can see that for example people can
[1072.24] ask questions and get help and we help
[1074.16] them like we are still here helping
[1076.08] people. However, I am not awake 24 hours
[1078.88] a day and I'm not always at my computer
[1081.28] and sometimes people are stuck on things
[1082.8] and it's not great to wait for like many
[1085.68] hours. And the thing is I often found
[1088.24] that people's problems I could solve not
[1090.56] necessarily by my great knowledge in my
[1092.4] head but rather by prompting AI
[1094.0] properly. And so quite often I would
[1095.52] just answer to people like a summary of
[1097.28] what I would get from an AI chatbot
[1099.2] connected to the knowledge base that I
[1101.68] have also in my workspace and you know
[1103.44] my notes and and all that stuff
[1104.96] basically. And then I was like wait I'm
[1107.04] becoming a copy paste machine again.
[1108.93] [laughter]
[1109.76] uh was like it's like it feels like
[1111.84] added value but really it isn't like
[1113.68] because it's like I wasn't doing much.
[1115.92] And so what I did is I built this little
[1117.76] age helper. Uh age helper is basically
[1120.16] that for this is my avatar. This is the
[1122.56] age helper avatar which is me uh as a
[1125.44] robot basically and the idea is
[1128.72] agehelper is always here to help you out
[1130.96] and whenever you post a question in the
[1134.4] uh get help section only then if it's a
[1136.8] technical question it's going to answer.
[1138.4] if it's not a technical question like if
[1140.08] someone's like super mad at us etc. is
[1141.76] actually going to skip answering and
[1143.44] it's going to wait for a human to
[1144.64] answer. So it's pretty smart in a way it
[1146.72] decides what to do. And so initially I
[1148.32] built it on my computer. So I would call
[1149.92] my computer and my computer would wake
[1151.52] up and we start it's built on codeex and
[1153.76] then it was connected to a whole
[1155.52] prompting system. It gives like these
[1156.88] pretty cool things these pretty cool
[1158.56] instructions and stuff. Sometimes it
[1159.84] even gives prompt for people to give to
[1161.52] their code. So that code solves the
[1163.44] problem for them. Like we've built all
[1165.2] that stuff and the idea is I get back to
[1166.96] them. And so how is it? Just to be clear
[1169.36] though, so you had this system like
[1172.4] internally that you were using to answer
[1174.24] a lot of questions. Yeah. Before
[1175.6] >> I did it manually. I had a skill
[1178.0] >> and then I was like, I'll make it a bot.
[1179.76] It run on my computer and then
[1181.36] eventually I was like, well, what if I'm
[1182.88] traveling? My computer is off. I run on
[1184.64] a laptop. I don't have a Mac Mini.
[1186.24] >> So from a skill to a bot to an
[1188.32] autonomous bot essentially.
[1189.52] >> Yeah, pretty much. That's where I'm at,
[1190.88] right? And now I'm actually expanding
[1192.24] it. So I'm building like DMs into it,
[1194.08] for example. So people can DM it and not
[1196.16] necessarily share publicly their issues
[1197.68] and it can help them because people are
[1198.96] liking it quite a lot actually. Um and
[1201.28] so
[1201.6] >> and and I want to be very clear as well
[1203.52] because I know a lot of companies will
[1205.36] be like oh I don't want to automate my
[1206.72] support. That's a bad experience. They
[1208.4] have you know horror stories from uh big
[1211.6] companies like PayPal that you can never
[1213.2] get through someone and you just keep
[1214.32] getting automated answers things like
[1215.84] that.
[1216.16] >> Yeah.
[1216.56] >> Well we've fully disclosed that this is
[1219.44] uh AI helper. Like if you come out of
[1221.36] this Gale, there's a big image at the
[1222.96] top of the get help section that
[1224.56] explains how the system works. Like
[1226.88] you'll get your AI helper reply and then
[1228.88] we will come and reply when we're awake.
[1231.04] >> And you can see I jumped in, right? It's
[1232.48] like I jumped in later and I was like,
[1233.84] "Yeah, I actually agree with what the
[1234.88] bot said." So yeah, whatever. [laughter]
[1237.36] >> So people are getting the best of both
[1238.96] worlds. They're still getting the same
[1241.04] answer or similar answer to what we
[1242.72] would have given them anyway. they're
[1244.24] still getting the marker gale kind of
[1246.64] oversight and they're also getting an
[1248.24] instant answer as well. And so when you
[1250.96] present it like that, then it's a
[1252.4] win-win for everybody.
[1253.84] >> Yeah, I agree. And it's like, you know,
[1255.12] for example, like Detroit this guy and
[1257.04] actually this was before I fixed the
[1258.4] formatting issue with the new bot, but
[1260.0] like this guy asked this complex
[1261.2] question and then AI helper gave him
[1264.24] like this answer and gave him the prompt
[1266.4] to give to code for like how to build
[1268.08] his strategy and everything. And
[1269.44] literally like people are like, "Oh,
[1270.8] this is super helpful. I hope to learn
[1272.24] how to hire someone like you later. So,
[1274.32] it's like it's actually a good thing,
[1275.76] right? It's like uh
[1276.8] >> I I think we get away with it a little
[1278.4] bit more because
[1279.04] >> because it's an AI thing,
[1280.0] >> AI, right? So, you do have to be a
[1282.56] little bit careful with that stuff, but
[1284.16] I mean customers getting instant answers
[1286.56] that are good.
[1287.44] >> Yeah. And then I DM
[1288.48] >> that's a very positive thing.
[1289.68] >> Then I jumped in. I DM'd him a skill
[1291.6] that I use for strategy and I was like
[1293.36] try to use this. And the point is this
[1295.2] guy has to Anyway, let's go back to how
[1297.04] this works. I don't think people care
[1298.24] too much about how we run things. And
[1299.92] so, how does this work? is like yeah
[1301.28] member ask and now what I've done is
[1303.12] actually the codeex instance that runs
[1305.12] this is on the digital ocean server
[1307.84] which means that it's always on and then
[1310.0] my computer can be off and it is just a
[1311.92] terminal on a digital ocean server I
[1313.76] think we pay $12 per month and it
[1315.28] basically operates that and I've worked
[1317.52] quite a lot on protecting it from prompt
[1319.52] injection and things like that so for
[1321.44] example uh it does not have many tools
[1323.84] it can only do web search and the
[1326.08] context of like the membership and all
[1328.16] the notes that we gave it for like
[1329.52] knowing what to and and the knowledge is
[1331.84] actually gathered by a third party
[1334.16] Python script. So it's kind of like
[1335.68] gathered by a script that runs before
[1337.76] and then it gives it to the bot as
[1339.84] context to use. Basically it just and
[1341.68] then the but can use that or not use
[1343.36] that. Then what happens is the bot can
[1346.0] only draft an answer and it doesn't even
[1348.08] interact with circle. So someone cannot
[1350.4] prompt inject it on like you know do
[1352.16] some crazy things on circle and then
[1354.08] what happens is just it passes text to a
[1356.88] script that uh then post the answer
[1359.68] which means like the script itself
[1360.96] cannot be prompt injected and can only
[1362.56] do one thing which is post an answer it
[1364.48] cannot interact in any other way with
[1366.4] circle so the point is like I've thought
[1367.76] a lot about security on these things I'm
[1369.44] a bit if you guys are in the membership
[1370.88] you know I'm a bit stupid on security
[1372.48] maybe but I care a lot about that and
[1374.24] it's not just a random codeex thing
[1376.4] >> stupid is the right word I think
[1377.44] paranoid is the right word I'm I'm a bit
[1379.68] scared. So basically I wasn't careful.
[1381.41] [laughter]
[1381.92] >> Uh and so the point is like
[1383.36] >> stupid would imply you're don't care
[1384.96] about it. So I the opposite.
[1387.04] >> I care about it a little bit too much
[1388.48] sometimes. So that's kind of the way I
[1390.0] built it. And it's quite interesting
[1391.68] because it has a filter. So the AI
[1393.36] before it answers basically decides if
[1395.44] it's going to answer or not. So in the
[1396.72] output it says post it or don't post it.
[1398.64] And it will help with like technical
[1400.08] issues for example and finding resources
[1401.84] on the thing. But like if someone's like
[1403.36] hey I want a refund or you guys suck or
[1405.28] whatever. um then it's not going to
[1407.84] start replying.
[1408.56] >> No, no one's posted that so far though,
[1410.4] right?
[1411.04] >> So far, it hasn't happened, but who
[1412.72] knows? That might happen one day. And if
[1414.48] it does, in principle, it should not
[1415.84] respond basically. And so that's the
[1417.68] idea. Now, one thing that's really kind
[1419.12] of cool with this bot is it, as I say,
[1421.12] it runs on codec cli, which runs on the
[1423.36] subscription, which means like this
[1424.8] basically runs like this whole thing
[1426.24] runs on 20 bucks per month subscription.
[1428.08] This runs on Gypy 5.5. So, it's a good
[1429.84] model. It's expensive as well, and
[1431.12] that's why the answers are so good. But
[1432.4] the point is if we paid API prices, we'd
[1434.16] probably pay hundreds of dollars. And
[1435.36] because I actually built it on a server
[1437.68] that can run a terminal, I can connect
[1439.92] it to a basically subsidized
[1441.92] subscription from OpenAI and therefore
[1445.04] reduce our cost significantly.
[1447.36] >> Is that kind of kosher or is that a bit
[1450.4] >> actually open is kind of cool with it.
[1452.56] So like if it was entropic, they would
[1454.24] not be cool with it. But like Sam Atman
[1456.24] came out and like if you pay for
[1458.0] subscription, you can use it however you
[1459.28] want and they're fine with programmatic
[1461.04] use or whatever. So it's like so far so
[1463.76] good. It might change in the future,
[1465.12] especially as need to turn more of a
[1466.56] profit. But right now, it's worth doing
[1468.88] for us. And that's kind of a tip for
[1470.32] those of you who care about that is that
[1472.24] if you run on something like a digital
[1474.32] ocean server, you could run the
[1475.52] terminal, you can run a subscription,
[1477.2] and you can save a lot of money. Like a
[1478.64] $200 subscription would give us like so
[1480.96] much. Like eventually, I could imagine
[1482.72] us expanding this, paying $200 a month
[1484.88] and get like basically unlimited usage
[1486.48] for all these bots, for all our needs,
[1488.64] our automated needs basically. That's
[1490.8] kind of how I see it. And then
[1492.08] eventually if they stop it.
[1493.04] >> Does that have to be a full-time 24/7
[1495.92] server? That would that work on like a
[1497.28] Cloudflare work?
[1498.24] >> No, it wouldn't. I don't think it would
[1499.84] work. Maybe it would. I I mean I'm not a
[1501.84] programmer so I'm sure there's like a
[1503.44] crazy way to make it work, but like out
[1505.2] of the box you kind of need like a
[1506.48] terminal. Uh and so that this runs on
[1508.32] Linux and it's a terminal and everything
[1510.08] and but you can run it on very cheap
[1511.68] server. I think the server we run is $12
[1513.6] per month. So yeah. And just to be clear
[1515.2] as well, like we really don't know the
[1517.2] ins and outs of all of the like, you
[1519.12] know, Cloudflare and Digital Ocean and
[1521.36] things like that. It's like Claude had
[1523.12] or Codex has built it for.
[1524.96] >> This is a proper vibe coding podcast.
[1526.96] Like we're talking about like it's like
[1528.72] even a lot of these logics on like I was
[1530.56] like let's just make it secure. Let's
[1532.08] brainstorm ways to make it secure. And
[1533.68] it was like okay well we need to prepare
[1535.12] for prompt injection. So we're going to
[1536.72] gather the context outside. We also
[1538.72] won't make it take any action. It's just
[1540.4] going to write text basically. So it
[1541.92] cannot do anything. You're not starting
[1544.32] by saying hey here are the five steps I
[1546.16] want you to follow. What you're doing is
[1548.0] you're saying I want it to this is the
[1549.92] outcome and I want you to think about
[1551.76] security.
[1552.48] >> Yeah. I'm scared of prompt injection.
[1554.24] How do we fix that? Uh update the plan
[1557.12] and then basically we'll do some
[1558.96] research and do it right.
[1560.08] >> It's almost like a good way to think
[1561.44] about it is like you're the like uh non-
[1564.8] techsavvy CEO talking to the CTO who has
[1568.96] to then go away and like build it. And
[1570.88] that CTO is now clawed or codec.
[1573.84] >> Yeah, exactly. You come with your
[1575.12] questions and your problems and then you
[1577.68] have it walk on solutions and now is
[1579.76] this going to be like, you know,
[1580.8] enterprisegrade solution. No, but like
[1583.92] for a bot that just answers on the
[1585.68] private community, it's fine. Basically,
[1588.32] >> and something that you said to me last
[1590.96] week actually was like try and push the
[1594.32] envelope out a little bit more. Um
[1596.56] because I think a lot of people they
[1598.64] have an idea of what they think AI can
[1600.72] do. Yeah.
[1601.92] >> Especially if you're kind of a bit of a
[1603.44] perfectionist and you're quite
[1604.72] particular about how things are done.
[1606.56] >> Um I'm sure a few people can relate to
[1608.24] that.
[1609.04] >> Then you kind of like tell it what it
[1611.68] needs to do. But if you just give it the
[1613.92] goal and the objective, you might be
[1616.0] quite surprised at like how capable it
[1618.08] really is. Now, and what I like to make
[1619.92] it do as well is I'm like, "Oh, instead
[1621.52] of trying to come up with things, just
[1622.96] do some research in like GitHub
[1624.48] repositories and how people are
[1625.76] addressing this problem, right? So, it's
[1627.12] it goes on like a bit of a web search or
[1628.72] it sends like a sub agent that does a
[1630.24] bunch of web search and that comes back
[1632.08] with useful context that then guides its
[1635.04] technical decisions. And so, you're kind
[1636.96] of piggyback writing technical people
[1639.76] that posted stuff on the internet
[1641.68] basically. So I'm not using codeex very
[1644.08] much at all right now but I'm building
[1646.24] most of my stuff in cloud code.
[1648.4] Sometimes when it does that it comes
[1650.88] back with like you know quite technical
[1653.12] program type language and I get a little
[1655.6] bit like I don't know what this means.
[1658.48] >> Quite often. Yeah. Yeah. quite often
[1660.64] inside my chats I just stop it and I
[1662.96] write Eli 10 what this means like
[1666.08] explain this like I'm 10 years old what
[1668.48] this means and it and it makes a very
[1670.08] nice analogy and it's just like oh okay
[1672.24] right I get that
[1673.28] >> exactly so it's just a lot of people do
[1674.8] that right they get an answer from AI
[1676.4] that they don't understand and they're
[1677.44] like oh that's it I'm in technical land
[1679.28] I can't do this and it's like they give
[1681.04] up but actually it's just like hey I
[1682.72] have no clue what you just said like
[1685.2] explain again quite often as well ask me
[1687.04] questions and it's like I have to make
[1688.24] decisions it's like oh do you prefer
[1689.6] using this uh this crazy branch of this
[1692.48] thing or do you want like to create a
[1694.0] custom CLA about the API? You know,
[1696.0] crazy technical terms. I'm like, I have
[1698.08] no idea what you're saying. Just just
[1700.16] rephrase this please in a simple way.
[1702.96] >> Another good one is like, all right, now
[1704.48] we need to set up the server and do this
[1706.72] and like that would be step one. Step
[1708.48] two would be this. And the answer is do
[1710.56] it yourself or just just do it for me.
[1712.08] >> It does that. It gives you walk and you
[1713.6] shouldn't do it.
[1714.64] >> Yeah. [laughter]
[1715.36] >> It's like I'm like no, no, no. I don't
[1716.8] do anything. still on the chat and uh
[1719.6] yeah that's one I think that's one thing
[1720.96] we talked about as well is like you
[1722.0] install the terminal tool and then you
[1723.28] just have it operate the terminal tool
[1724.8] and you don't leave your chatbot the
[1727.04] truth is the most of this customer
[1728.72] support I built on my phone I built on
[1730.72] the Codex app by just talking to it like
[1732.88] a walkie-talkie while walking my dog and
[1735.52] most of actually a lot of my codeex
[1738.48] building time is on my phone now and
[1740.24] just kind of talking into it at the gym
[1742.88] outside whatever or even like on my sofa
[1745.36] end of the day when I'm super tired and
[1747.04] just get ideas for features. So, for
[1748.4] example, like last Sunday, I was like,
[1749.76] "Ah, would be great if people could DM
[1751.6] and kind of talk about more sensitive
[1753.04] topics with the bot cuz it's pretty
[1754.32] helpful." And then it's like I already
[1755.76] have a feature that's set up now. It's
[1757.52] not live, but it works. And then it's
[1759.28] like I need to test it more. But like uh
[1761.12] eventually,
[1761.92] >> you are you reading the response it gets
[1763.76] or do you have it like text to voice
[1765.84] into an AirPod or something?
[1767.28] >> I like to read like I'm a I'm a reader,
[1769.52] but everyone to their own like if you
[1772.08] want it, you could do that. Uh but yeah,
[1774.0] anyway, that's the support bot. It's
[1775.76] kind of handy. And again, that could be
[1777.52] answering customers emails, that could
[1779.2] be helping with technical questions,
[1780.96] that could be anything like eventually I
[1782.16] want to make it almost like an API. And
[1784.0] I want to plug it into all our customer
[1786.64] support channels basically. So that's a
[1788.4] VIP code project that went all the way
[1790.16] from a scale to like a proper bot that
[1792.24] runs.
[1792.96] >> Nice. I want to move on now and talk
[1795.36] about something which I first heard
[1797.36] about when back in the day when I had a
[1799.04] real job in a large enterprise company.
[1802.16] It's called data warehousing. And it's
[1804.64] one of those terms that sounds like kind
[1806.24] of corporate bingo that I just
[1808.0] like, oh, send me to sleep now. Kill
[1810.24] kill kill me now.
[1810.88] >> It sounds boring.
[1811.52] >> It sounds boring, but it's super cool
[1815.36] when you don't have to do any of the
[1816.8] work behind it and you just kind of give
[1818.08] it the guidance to do it. So, do you
[1819.84] want to explain what the problem is
[1821.76] we're actually trying to solve with this
[1823.28] and how we built this warehouse of all
[1825.6] our data?
[1826.4] >> And I actually have this little image
[1827.68] that was prepared for that. And
[1828.88] basically, it's the idea of creating one
[1830.48] database that has every single event
[1832.08] that happens in your company. So if you
[1833.92] look at what we do for example, we
[1835.84] collect payments on stripe. When people
[1838.24] check out it comes there. People use our
[1841.28] product on circle which is like a
[1843.36] community platform. So whether they
[1844.88] watched a video, they logged in or they
[1846.8] liked something or whatever like that
[1848.24] data lives there. Then we do email
[1850.32] marketing with a tool called Bento.
[1851.92] Again they have all our open rates,
[1853.44] their click rate, when people
[1854.96] subscribed. We also track like you know
[1857.36] when subscribers visit certain pages on
[1859.28] the website for example that kind of
[1860.72] stuff. It's pretty handy for like signal
[1862.4] of whether people are going to buy or
[1863.76] not. Uh we have all our support
[1865.6] questions on help scout which is another
[1867.44] support platform. And then we usually
[1869.6] collect kind of like forms through an
[1871.92] app called EU form, right? And then
[1873.36] there's even more.
[1874.0] >> The reason the reason we use euform by
[1875.68] the way is because we got this amazing
[1877.2] lifetime deal on it many years ago and
[1879.52] it's it's been brilliant.
[1880.8] >> The truth is you could v code a U form
[1883.52] in about 30 minutes I think now. But
[1885.76] it's finally
[1886.56] >> 30 seconds now probably. Um, honestly,
[1889.12] it's so well built and so nice and it
[1891.68] integrates with everything. It's just
[1892.96] like cool, we just use that.
[1894.4] >> But the truth is,
[1895.2] >> you know, they even have an AI agent
[1896.56] that I now get prompts to copy paste
[1899.28] into that agent and it just builds the
[1900.96] form for me as well. So,
[1902.08] >> okay.
[1902.8] >> Okay. Not bad. But yeah, still you could
[1904.48] just V code.
[1905.12] >> How about you form by the way? Yeah.
[1906.8] >> Yeah. So, anyway, we have all that
[1908.4] business data living in different
[1909.6] places. But the thing is like the story
[1911.28] of a customer lives across all these
[1913.2] platforms, right? So, it's like they
[1914.4] might have some support tickets, then we
[1916.24] have some activity data here. we know
[1918.08] what they paid on Stripe etc. It's kind
[1920.0] of difficult to tell for example like is
[1921.6] a customer about to cancel for example
[1923.44] which like to tell that you need to be
[1925.12] able to know when their payment plan
[1927.6] ends for example their level of activity
[1930.08] are they subscribed or not to the list
[1931.6] did they complain about anything on
[1933.2] helps card or like is there any activity
[1935.36] from any form that we have and then if
[1937.04] you combine all that data you can start
[1938.72] telling the story of where this customer
[1940.56] is at with your product but individually
[1942.56] each of these things doesn't really help
[1944.24] you tell the story and so what we v
[1945.92] coded was basically just a simple way to
[1948.64] send all the data of all these platforms
[1950.8] into one big company database that we
[1952.72] host on Superbase. You can start for
[1955.04] free. We pay $25 per month for that. Uh
[1957.92] right now, mostly because we actually
[1959.28] process quite a lot of data. Uh and but
[1961.76] it's fine like we will be
[1963.12] >> I mean that's it's crazy compared to the
[1964.8] like the hundreds of thousands of
[1966.64] companies pay for some like Oracle or
[1968.8] you know one of these big enterprise
[1970.72] database systems.
[1971.76] >> And that's kind of the thing with small
[1972.96] businesses, right? We've always had all
[1974.4] that data in all these tools, but we
[1975.84] never really made use of it because it
[1977.28] just was too much time, too much effort,
[1978.88] and too difficult technically to do it,
[1980.56] right?
[1980.8] >> And because it's in different places.
[1982.08] Yeah. It's difficult to do.
[1983.2] >> It's just it was difficult like
[1984.32] connecting APIs, all of that. It just
[1985.92] breaks and you have to update it and you
[1987.76] know what I mean? Like and so now we can
[1989.2] actually go on code and for example, you
[1990.64] know, I said use superbase, which is the
[1992.32] database, and tell me how many member
[1993.6] subscriptions are expiring this week.
[1995.2] And I can tell exactly that there are 14
[1997.04] memberships expiring this week. And I
[1999.04] can tell, you know, like one that is
[2000.4] expiring, so they already cancelled.
[2002.08] there is four that are renewing for sure
[2004.0] and these are actually unknown. So I
[2006.24] would need to dig deep and then I could
[2007.6] say like okay which of these members are
[2009.04] at risk for example and what it would do
[2011.28] would get is it would get the data from
[2013.2] circle and it would say which ones did
[2014.72] not log in for example in the last 14
[2016.4] days or something and we just kind of
[2017.92] highlight them to me and I say then
[2019.68] please email them and propose them to
[2021.76] have a free catchup call with me for
[2023.12] example and then all of a sudden I can
[2025.44] reactivate these people and they can
[2026.72] keep paying me and that was literally
[2028.32] three prompts on cloud code now it's
[2030.0] connected on the database and so that's
[2033.12] what this database does is it allows us
[2035.04] to get visib ility and take action and
[2037.36] not only us take action but the AI takes
[2039.6] action on people basically and we can
[2042.64] just optimize our revenue just by being
[2045.52] helpful to the right people at the right
[2046.8] time basically.
[2047.6] >> Yeah. And because that now cloud code
[2050.32] has access to that anytime we do
[2052.32] something that touches members. So a
[2054.16] good example would be the member survey
[2056.64] we did a couple weeks ago. So we got
[2058.88] about 250 people to reply, fill in like
[2061.6] eight or nine questions multiple choice
[2063.44] and there was usually we used to do just
[2065.76] multiple choice questions on surveys but
[2067.6] now because we have AI analyze it we had
[2069.76] like an open text field for you know
[2071.44] like what could we improve you know the
[2073.04] questions like that and it was able to
[2074.8] not only analyze that but cross that
[2076.64] data against with what was in the
[2079.28] superbase database you know what type of
[2081.68] member are they how active are they and
[2083.84] you know we can see like what are the
[2085.12] active people doing what their lifetime
[2087.52] big spenders.
[2088.48] >> Yeah, exactly. So, it's like you don't
[2090.16] just take the survey output, you just
[2091.92] actually can wait it for like how much
[2093.52] revenue that is for you and which
[2094.88] segment you should optimize for that
[2096.48] kind of stuff and that changes
[2097.52] everything. Basically, you don't just
[2099.04] data
[2100.08] >> instead of Gail and I, which we were
[2102.08] actually doing having like quai
[2104.72] arguments about like no our members need
[2107.28] this. This is what they want. This is
[2108.64] what they hate. This is these are the
[2110.0] problems. We're like why are we let's
[2112.16] just ask them and then have AI figure it
[2114.08] out. And it did.
[2115.2] >> It was good. Being able to get that
[2117.52] level of insight about your business and
[2119.36] your customers and what they need and
[2121.36] where you should take your product is
[2123.52] invaluable. Every business needs to do
[2125.6] that.
[2125.84] >> I mean consultants pay like charge
[2127.6] literally tens of thousands of dollars
[2129.04] to do that and all we did was like a
[2130.48] Google
[2130.8] >> millions of dollars millions of dollars
[2132.72] for like Mckenzie to go into an
[2134.24] enterprise.
[2135.36] >> Most of our listeners don't hire
[2136.96] McKenzie. So probably the level of
[2138.96] consultants they will hire will be tens
[2140.56] of thousands. Uh
[2142.08] >> I'm just saying like the same way um
[2144.64] building a lot of infrastructure you
[2147.12] know with code was out of reach for
[2148.8] small business because code used to be
[2150.4] expensive now things like having a not
[2153.92] it's not really a consultant but like
[2156.08] this level of data analysis it was
[2158.4] completely out of reach before because
[2159.68] it was so expensive but now everyone can
[2161.76] do it. It's a great equalizer.
[2163.84] >> Yeah. And just to explain quickly the
[2166.72] technical way how it works is basically
[2168.48] every time something happens there's
[2169.84] something called a web hook in these
[2171.04] apps. So for example, Stripe sends a web
[2172.72] hook and it's like it sends data to a
[2174.64] Cloudflare worker and that Cloudflare
[2176.16] worker basically cues it to update to
[2178.4] Superbase and then every 15 minutes
[2180.64] depending on which APIs it will actually
[2183.6] query the API to see if it missed any
[2186.16] event basically and it just kind of
[2187.36] updates itself and the idea is like the
[2189.2] data is constantly updated like every
[2190.88] time someone likes a post on Circle,
[2192.64] every time someone logs in, every time
[2194.08] someone clicks on an email, every time
[2195.52] someone opens and we can just reconcile
[2197.28] that into member profiles and we get
[2198.88] like full data basically. It's very very
[2200.64] cool. You should do that if you have any
[2202.8] customer data. And one thing about the
[2204.16] survey that you didn't mention as well
[2205.2] is like the survey was only like seven
[2207.12] or eight questions. It was very small
[2208.8] which was easy to do for people. But at
[2210.4] the same time, because we could cross it
[2211.6] over with the data, we got an insane
[2213.12] amount of insights actually. And so like
[2214.96] it goes well beyond what you imagine
[2216.72] when you do that. And you don't even
[2218.08] need to know what you're doing. What we
[2220.32] did is we're like here's the survey
[2221.52] output, use the database and figure out
[2224.48] what people want basically and focus on
[2226.56] like and help us segment people by
[2228.8] revenue activity etc. and do all these
[2231.36] segments and that's it and we got it. So
[2233.68] yeah, that's pretty powerful. So yeah,
[2235.52] you can ask all these questions that who
[2236.88] might cancel soon, who applied to our
[2239.44] plus level, was that person's full
[2241.36] history? And yeah, Cloudflare, we pay $5
[2243.68] per month. Superbase, we pay $25 per
[2245.44] month. And these APIs are usually
[2246.96] included in whatever tool you're paying
[2249.76] for. So it's not expensive basically.
[2251.92] >> Yeah. And the interesting thing about
[2253.84] building on Superbase is you can
[2256.4] actually kind of build software within
[2261.52] there. Let me sort of talk you through
[2263.52] an example here. So they have something
[2265.52] called edge functions which is as far as
[2268.0] I understand a little bit like a
[2269.52] cloudflare worker but it's kind of built
[2271.44] directly into superbase.
[2273.52] >> Yeah, that's correct.
[2275.28] >> Yeah. Am I right there?
[2276.24] >> That's correct. That's correct.
[2276.82] [laughter]
[2277.36] >> It's waiting to be you don't even know
[2279.2] what we built. It's fine. It's true.
[2281.28] >> Yeah. This is the point like I don't
[2283.36] [laughter] like
[2284.0] >> but it's working right.
[2285.04] >> But I still have this work like I built
[2286.64] this yesterday in like couple hours. So,
[2289.52] we now have a cancellation or refund
[2292.8] form on our website. Again, shout out to
[2295.36] you form AI uh gave me all the prompts
[2298.64] to build this. So, when somebody fills
[2300.56] that in uh and they want to cancel their
[2302.88] subscription, we get some data and we
[2304.8] ask them like why they're cancelling and
[2306.4] you know what we could have done to
[2307.68] convince them to stay. Very, very useful
[2309.52] information to have. So, what happens is
[2311.68] they'll fill in that form. Um, we have a
[2314.08] quick check to make sure it's not a bot
[2315.68] and you know that form's not getting
[2317.84] spammed. Um, but then it sends that data
[2320.48] into Superbase, but the edge function
[2324.24] within Superbase is essentially like
[2326.48] this agent that spawns up and starts
[2328.96] doing a few different tasks here. So,
[2330.72] it's going to look up all the data about
[2333.2] that member. So, for example, which
[2335.28] courses have they taken, which lessons
[2336.96] have they been through, how much have
[2338.64] they paid, how long have they been a
[2340.0] member, like those types of things. and
[2341.92] it's going to use all of that data to
[2344.0] then generate a response to their
[2347.84] cancellation request. So, you know, if
[2350.48] they just want to cancel, like, hey,
[2352.24] this isn't for me. I'm not interested.
[2353.68] Fine. I'm not going to try and stop
[2355.2] anyone. But if they're like, oh, it was
[2357.36] too difficult and I couldn't figure out
[2358.88] how to do this and this. Then that's an
[2361.76] opportunity for us to save that sale and
[2364.64] to offer them a solution to that. That
[2366.72] may be directing them to the relevant
[2368.48] content. that might be, you know, some
[2370.72] kind of discount or promotion or some
[2372.8] kind of offer that we can give to people
[2374.16] that way. And being able to do that in a
[2377.92] highly tailored and personalized way is
[2380.56] really, really valuable because, you
[2382.48] know, we've all been through these
[2383.6] cancellation process before and it's
[2385.2] like you get a generic, hey, you know,
[2388.0] you're trying to cancel, here's a free
[2389.76] month or something like that and it's
[2391.12] like you don't really care about me.
[2393.04] This is just your automation. But in
[2394.72] this way, we're giving people a more
[2397.28] custom kind of experience of this and
[2399.68] kind of really helping them to solve
[2401.12] their actual problems in there. So, how
[2403.12] that looks at the end is when someone
[2405.12] fills in this cancellation form, it has
[2407.76] this decision logic in here. So, you
[2409.52] know, are they eligible for a refund?
[2411.04] What's their the kind of monthly billing
[2413.2] uh cadence? You know, those types of
[2414.72] things, what's set and what's not. And
[2416.88] then it's not going to send them, it's
[2418.24] going to draft them a reply. And so,
[2420.8] this is a super super basic reply. By
[2422.72] the way, I just built this yesterday,
[2424.16] but it shows you what you can do with
[2426.0] it. And I can just go in there and edit
[2428.8] that as I want or just send it as it is.
[2431.36] And and we're kind of good to go from
[2432.8] there. The edge function itself is
[2435.84] receiving the data from the U form. So
[2438.48] from the ticket, it's using GPT 5.5 to
[2441.52] draft a reply using all of that data and
[2444.24] then sending that draft into Help Scout
[2446.08] or customer support software. Uh, and so
[2448.72] all of that, which would have taken me,
[2450.88] you know, 5 10 minutes to do, and I
[2453.28] wouldn't even have been able to do all
[2454.72] of the stuff in there because there's no
[2456.24] way I'm going through all of their data
[2457.68] and all of their, you know, view history
[2459.52] and lesson history every single time.
[2461.6] It's like it's just not feasible to do
[2463.76] that. It does all that in literally like
[2466.72] seconds. Uh, because it's the edge
[2469.2] function sits right inside Superbase, so
[2471.12] it can access the data really, really
[2473.2] quickly. There's like zero delay there
[2475.68] basically. So yeah, this is something
[2478.16] that I built on top of the database that
[2480.08] Gail set up there.
[2481.2] >> Yeah, and that's the thing. We can now
[2482.64] start building all these stuff and do
[2484.96] that basically. It's really cool. Just
[2487.12] wanted to say one thing about the model
[2489.92] selection because people were like, "Oh,
[2491.04] why are you using GT5.5?"
[2492.96] And the reason is because actually GT5.5
[2495.76] is actually a very uh efficient model.
[2498.72] It's very cheap if you run it in low
[2502.16] reasoning and medium reasoning. And I
[2504.0] actually have some data to prove it. So
[2505.44] this is artificial analysis and a lot of
[2507.52] people run on 4.6 which is kind of like
[2510.56] considered like a costefficient way to
[2512.8] do which is not much cheaper than Opus
[2514.64] anymore by the way. Opus is almost the
[2516.4] same price was $4,200. But if you run
[2518.8] G5.5 in medium or low you can see G5.5
[2522.08] medium did the same test for $1,199
[2524.96] and low did it for $500 which is pretty
[2527.6] good. Uh and it's actually like almost
[2530.32] on par. It's almost on par with Gemini
[2532.32] 3.5 flash actually if I put it in
[2534.56] perspective. So if I put 3.5 flash in
[2537.2] there actually 3.5 flash high is here.
[2539.12] Yeah, it's actually higher. 3.5 flash is
[2541.04] $1,500 and GP 5.5 medium is $1,200. So
[2545.52] actually 5.5 if you use it as like not
[2549.6] maximum reasoning is actually a pretty
[2551.36] good cost efficient model that writes
[2552.96] pretty well and is pretty smart
[2554.24] basically. So my recommendation right
[2555.92] now and I used to recommend flash but
[2557.52] flash got expensive is to actually use
[2560.24] 5.5 in low or medium reasoning for bang
[2563.2] for your buck for API actually. So yeah
[2565.68] it's like that's the kind of vibe coding
[2567.52] projects I guess that that was the last
[2569.04] one right?
[2569.76] >> Yeah that's I mean that's everything
[2571.2] we've been through quite a lot there but
[2573.52] just wanted to kind of give everyone a
[2575.36] practical behind thescenes look at the
[2577.36] stuff we're actually building hopefully
[2579.36] to give you guys some similar ideas
[2581.44] really.
[2581.76] >> And it's the stuff that's like not
[2583.04] flashy. It's kind of internal mostly,
[2585.2] but that's what I mean it's allowed us
[2587.04] to run this whole thing almost just us
[2590.16] because like literally like the product
[2592.24] is getting a lot of assistance. The
[2593.84] support is getting a lot of assistance
[2595.84] and then in the end like we still have
[2597.36] to kind of manage a lot and we're in a
[2598.96] process of like automating anduling a
[2601.04] lot more things now. But in general like
[2603.2] that's the kind of like vibe coding
[2604.96] projects that you should undertake in
[2606.72] your company that will make a
[2607.92] difference. It doesn't have beautiful
[2609.52] front end. It doesn't have any of that
[2611.44] but it actually will save you a ton of
[2613.36] time and you just need to learn a few
[2614.56] things like learning superbase learning
[2616.48] cloudflare workers for example and then
[2619.12] playing a little bit with API
[2620.4] >> just to be clear you don't need to learn
[2622.0] that you need to learn they exist what
[2624.56] it does to yeah what it does so that you
[2627.52] can kind of talk to AI and it will do it
[2629.44] for you
[2630.0] >> yeah so like most of these things like I
[2632.08] could see when you presented the superb
[2633.44] stuff you basically didn't even know
[2635.36] >> yeah [laughter] like I don't really know
[2638.32] what it is
[2638.88] >> it's probably worse like you know all
[2640.64] these tools both code and codeex they
[2642.8] have security review plugins it's
[2644.88] probably worth running your code through
[2646.64] that if you're vi coding these things it
[2648.48] will help there are special tools as
[2650.32] well there's tools like code rabbit etc
[2651.84] that help catching issues but the truth
[2653.44] is the best models like don't use a
[2655.04] cheap model but the best models they
[2656.48] have a lot less security flows now than
[2658.32] they used to have like these kind of
[2659.6] like nightmares of vip coding etc it's
[2661.52] not as bad as it used to be doesn't mean
[2663.2] it can't exist doesn't mean you
[2664.32] shouldn't check but it's less much much
[2666.8] less likely than it used to be even a
[2668.4] year ago
[2668.8] >> and you can We're still quite cautious
[2670.64] around things like look, it's not
[2672.24] sending messages and support. It's
[2674.32] drafting them. It's not it has no access
[2676.96] to payments or, you know, anything like
[2678.88] that.
[2679.76] >> Uh so, you know, there's there's some
[2681.92] hardcoded like walls that it just can't
[2684.4] do and can't get access to, but we're
[2686.0] generally quite cautious about this
[2687.2] stuff. We're not vibe coding our
[2688.96] shopping cart software. We're using
[2691.04] like, you know, established companies to
[2693.68] do that. So,
[2695.04] >> yeah. I mean, I think sometimes what
[2697.68] pisses me off is on social media, even
[2700.72] on YouTube, a lot of the examples that
[2703.68] people share are like, "Here's how I
[2706.08] create content or do some like flashy
[2708.4] visual thing using AI." But the truth is
[2712.88] 90% of businesses out there, they're not
[2715.68] content businesses. They're not social
[2718.24] media influencers. they have a product
[2721.04] or a service and they kind of like
[2722.64] deliver that and it's it's kind of a bit
[2724.72] boring sometimes and it's that boring
[2726.8] stuff that you need to work on
[2729.36] automating because that is the core of
[2731.12] your business. you automate this stuff
[2733.2] and then you make content still
[2735.84] involving yourself because I think
[2737.28] that's the hardest thing like sure you
[2738.64] can do as love you can make like a baby
[2740.48] podcast and then you get lots of views
[2742.64] on Tik Tok you won't make much sales if
[2744.64] you want to make sales and if you want
[2745.76] to sell stuff it actually is worth doing
[2748.16] the human stuff that people connect with
[2750.32] still like with AI assistance but like
[2752.64] not necessarily fully automated I don't
[2753.92] make like a clone of myself on a gen and
[2755.92] post videos about that for example and
[2757.84] then just basically take everything else
[2759.76] away with AI and that part is almost
[2762.48] invisible to people and so you're not
[2764.48] dropping your quality, you're not
[2766.0] discounting your brand or anything like
[2767.44] that and things like the database. Yeah,
[2769.68] if anything it makes the experience
[2771.04] better for people. So that's what you
[2773.44] should focus on. I know we get a lot of
[2775.12] people like how do I make content with
[2777.04] AI? I reluctantly do a little bit of it,
[2779.28] but I'm not a big fan because I actually
[2781.2] think that's not what they should focus
[2782.56] on. Uh what they should focus on is
[2784.72] automating what they sell and all the
[2787.84] service layer around what they sell. And
[2789.6] then the content part is now you have
[2791.68] time to do it and then you actually have
[2793.28] a chance because most people who like
[2794.88] fully automate their content with AI
[2796.64] like point to me apart from a few
[2799.04] YouTube channels or Tik Tokers or
[2800.72] whatever there's not a lot that
[2802.48] >> but even then they have the high high
[2804.24] views but like are they really you know
[2806.08] like making a lot of money and selling a
[2807.76] lot of product off the back of that.
[2809.84] >> Everyone dreams of doing that. I mean,
[2811.12] sure, with SEO show, I'm sure you can
[2812.64] point at some of it, but like for
[2814.24] anything else, like, I'm sorry, but
[2816.0] like, show me a real business channel
[2818.16] that makes a lot of money with the fully
[2821.12] AI generated content. However, show me
[2823.6] businesses that v code these kind of
[2824.88] projects. We show many of them,
[2826.24] actually. So, yeah, that's the final
[2828.64] words of wisdom, I guess.
[2829.84] >> Okay, brilliant. Well, thanks for tuning
[2831.84] in to this episode of the podcast. We're
[2833.76] only really able to go in depth with
[2836.4] this stuff in a long format piece of
[2838.88] content like a podcast like this. So,
[2841.52] thanks. It's an hour long. Appreciate
[2843.12] you staying to the end. Make sure you're
[2844.96] subscribed because we're going to be
[2846.4] doing a lot more episodes like this. If
[2848.88] you enjoyed it, head on over to our
[2850.8] YouTube channel. Um, just search for
[2852.56] Authority Hacker, find the episode
[2854.16] there, and leave us a comment. Tell us,
[2856.64] do you like this type of format? Do you
[2858.48] want us to show us more quote unquote
[2860.72] boring automations uh from our business
[2863.12] and things that you could do as well in
[2865.04] your business like this? We'd love to
[2866.8] hear your feedback on that. So, thanks
[2868.72] for listening and we'll see you again
[2870.72] next week for another
