# Transcript

**Expert:** Marvomatic_AI_Automations

**Video ID:** FIYwJPPdtug

**Collected:** 2026-06-25 07:20:07

---

[0.08] Let me show you two workflows that I am
[1.92] using for first of all analyzing data
[3.92] from my Google search console to find
[5.52] content gaps. So which is this one but
[7.84] also another workflow that takes care of
[10.56] analyzing the data again and then it
[12.4] creates complete articles based on the
[14.88] content gaps and the output is actually
[17.04] quite simple. So we have the content gap
[19.28] analysis which is this one. So how many
[21.68] pages were analyzed total keywords but
[23.76] what's more important or I would also
[25.76] say the most important part is the
[27.52] content opportunity section. So as an
[29.6] example in this analysis was also the
[32.16] page included maromatic.com products and
[35.2] 14 keywords were analyzed and it found
[37.76] out that there were like two content
[39.36] opportunities which is automate click
[41.76] with click z3 and also complex and end
[44.88] workflow but the good thing is that you
[46.8] have for every page you want to analyze
[48.8] a specific analysis. So let's say I want
[51.2] to check this page here then I can also
[53.12] see top keywords by impressions content
[55.76] gap opportunities. So in this case, it
[58.16] might make sense for me to create a
[59.76] piece of content that is targeting the
[61.52] keyword and an image analysis because
[63.76] I'm already ranking on position 20 with
[66.96] this specific page here and has nothing
[69.2] to do with image analysis. So if I take
[71.76] this keyword, create a new piece of
[73.6] content, link this piece of content with
[76.24] my other articles and vice versa, then
[78.32] the probability is quite high that I
[80.08] will rank for this specific keyword here
[82.24] with my new page. And that is exactly
[84.48] the reason why I've created this
[85.92] workflow because it is able to analyze
[88.0] the data. But what's more important, it
[90.08] can create another dashboard that shows
[91.92] me exactly what kind of content makes
[94.48] sense to create for this specific
[96.24] keyword. So here we have complex and end
[98.16] workflow. And we have always the
[99.6] article. So in this case, it's 186
[102.56] words. So quite long. We have also
[104.72] internal links and also external links
[106.8] because this workflow here knows exactly
[109.84] which page was analyzed and then it
[112.4] creates automatically a link back to the
[115.04] specific page. So you don't have to do
[117.52] it manually. But since we are also
[119.68] scraping data from the Zer results, we
[121.6] can also display data such as an outline
[124.64] based on the competitor's data questions
[127.2] which were extracted by Zer results,
[129.2] content gaps, links and so forth. So
[131.36] it's quite comprehensive. In case you're
[133.68] interested in such workflows that help
[136.0] you definitely to grow organically your
[138.72] visibility with a datadriven approach
[140.88] then you can find it within my community
[143.2] under n templates and it is in the
[146.64] folder datadriven content gap analysis
[149.28] which is here. So there's also another
[151.44] video where I explain exactly how the
[153.2] content gap analysis workflow works and
[155.28] as you can see I have also a lot of
[157.36] other workflows including step-by-step
[159.6] instructions on how to set them up. So
[161.6] in case you're interested in first of
[163.36] all learning how to create workflows for
[166.08] search engine optimization by using NN
[168.4] then you will find here a lot of good
[170.0] resources. All right then let's have a
[171.92] look into the logic of these workflows
[174.64] and everything starts actually with this
[177.04] one because as you can see this workflow
[179.84] here is triggered as a subworkflow and
[182.72] the same for this workflow here. The
[184.72] workflow that actually starts a complete
[186.72] analysis is this one. So we have here a
[189.84] menu trigger. You can also add a
[191.28] schedule trigger, but I like to perform
[193.92] this analysis kind of manually. So we
[196.24] just click on it and then it gets the
[198.32] URLs which are here in this Google
[200.32] sheet. So we have all the URLs from the
[202.4] website including the domain. So in case
[204.96] you want to add more pages, it's really
[207.28] easy. You just have to enter it here.
[209.36] And of course you can also add other
[210.96] websites then you just have to configure
[213.2] this sheet here. So at the domain and
[215.6] also the name for the big query table
[218.16] which also means this workflow here
[220.8] works only if you have access first of
[223.04] all to the Google search console and
[224.8] ideally also the bike data export
[227.36] activated
[229.04] and after that the first step is to
[231.12] split out the pages in case you want to
[233.52] do a test run then I highly recommend to
[235.6] always set a limit. So I also did for
[237.44] the demo a limit for five pages and then
[240.64] the first step is to get the keywords
[243.04] from big query. So we have here custom
[245.28] SQL query that is able to extract low
[248.32] hanging fruit. So it has a focus for
[250.4] longtail keywords. But what's more
[252.08] important is that it's not using hard
[254.72] thresholds and instead it calculates
[257.04] them dynamically based on the
[258.64] performance for the specific page. It
[260.72] means if you have a website with a lot
[262.8] of articles and let's say 10% get a lot
[265.44] of traffic then they would use different
[267.44] thresholds than a page that you
[268.96] previously added where you don't have a
[270.72] lot of traffic yet. After that we take
[273.2] the keywords and also the extracted page
[275.68] content. So here we are crawling the
[277.44] page. Then we get the meter data as an
[279.6] example. We get the title, description,
[282.56] content and the URL. And then we pass
[285.04] all the data to a large language model
[287.76] with the task to analyze the keywords
[290.64] that were extracted from the Google
[292.08] search console data including the
[294.0] article and then it flags the keywords
[296.56] with either if it is a valid new content
[299.2] idea. So we have here the aggregate node
[301.36] and then we can see we have the
[303.04] keywords. So the potential new topic
[305.2] might be automated website traffic
[307.2] reports and then we have also the key
[309.68] value pair which is is valid new content
[312.24] idea. And if this is classified as true
[315.6] then it will eventually be used for the
[318.08] next sub workflow which is fill content
[320.64] gap. So this one here and the first step
[323.28] is to analyze the tone. So as an example
[325.68] we have here prompt and also the
[327.44] complete article otherwise it wouldn't
[329.52] be possible to analyze the tone and also
[332.32] the kind of writing style that is used
[334.64] on the specific website. After that we
[337.76] cluster the keywords that were extracted
[340.08] from this specific node here and once we
[343.04] have the clusters we take them and then
[345.6] we loop over every cluster and create a
[348.16] new article for that specific query and
[350.96] the subprocess starts first of all with
[353.36] getting data from the zer results by
[355.92] using the API from data for SEO. After
[358.88] that, a code node is used for ping this
[361.36] data to make it more readable for the
[364.0] next LLM calls, but also to get rid of
[366.96] information that is not important at all
[368.72] because the less data we pass to the
[370.96] large language model, the less tokens we
[373.12] will consume, which eventually means the
[375.44] workflow will be more cost effective.
[378.08] Once we have the data from the Zer
[379.68] results, we also know which pages are
[382.16] ranking and the top positions which
[384.4] allows us to take the URL, pass it to
[387.04] the API from fire crawl, get the
[389.2] content, aggregate it and then pass it
[391.44] to a large language model that is used
[393.76] for the competitor analysis so that we
[395.68] know exactly what kind of headings are
[397.76] they using, how long is the content, so
[400.32] the overall structure which will be used
[402.8] as a guideline to create the new article
[405.04] for our page. After that we pass the
[407.52] data. So as an example the previous LLM
[410.24] node gives us a content brief including
[412.4] a title meter description how many words
[415.68] we should target the content type which
[418.08] is in this case a guide and what's also
[420.48] important the outlines. So, which
[422.96] headings should we use for our article
[425.52] based on the competitor data? And to
[427.92] make that even better, we also use the
[429.92] API from perplexity to research the
[433.12] content so that we won't use any
[435.52] outdated information first of all from
[437.76] the trained large language model, but
[439.68] also from the articles that we scraped
[441.84] from the competitors, which means
[443.52] eventually a lot of data gets passed to
[446.16] the node generate article with a lot of
[449.04] variables. So we have some rules so that
[452.08] in case it writes an article with the
[454.16] title best ideas for a specific year
[457.2] then it won't use 24 23 or whatever year
[460.56] it has been trained on that's the reason
[462.48] why we add here also the current date as
[464.8] an alternative would be also possible to
[466.64] use an AI agent and then equip it with a
[469.6] tool to get the current date but in this
[471.68] case I wanted to keep it as simple as
[473.52] possible then we have the brand voice so
[476.32] what kind of writing style should be
[478.08] used so that is a part that was analyzed
[480.88] in the first note. Then we have the
[482.64] content brief, an article outline, all
[485.04] the questions that were extracted from
[487.2] the ZER results, content gaps that
[489.2] should be filled. And as you can see,
[491.2] there's much more data that is
[493.04] eventually used for generating the
[495.76] article outline, questions, gaps,
[498.24] titles. So everything that you can see
[500.4] here. And the last step in the
[502.24] subprocess is to grab this data from
[504.96] this note here pass it so that first of
[507.12] all we are also able to use that data
[510.56] here for storing it somewhere else. So
[512.48] in case you want to store it in a table
[514.64] then you could simply for instance here
[516.8] Google sheet note air table or something
[518.72] similar
[520.24] and then grab the key article markdown
[522.32] but also the title meter description and
[526.4] all the other data that is displayed
[528.08] here. I do think this is definitely a
[530.48] nice approach for automating the first
[532.8] of all content gap analysis but also the
[535.04] part of creating new content for the
[537.6] specific queries that you're already
[539.36] ranking for. And that's it already for
[541.68] this video. So in case you have
[543.12] questions to either the cont gap
[545.44] analysis or any questions related to the
[548.16] process of generating new content with
[550.72] this specific workflow here then feel
[552.72] free to add them to the comments and we
[554.4] will see each other in the next
