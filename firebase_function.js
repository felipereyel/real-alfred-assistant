'use strict';

const { dialogflow, SimpleResponse } = require('actions-on-google');

const functions = require('firebase-functions');
const fetch = require('node-fetch');

function getContentFromAPI() {
	return fetch('http://realalfred.pythonanywhere.com/new')
    .then(res => res.json());
}

const app = dialogflow({debug: true});

app.intent('checar novos episodios para serie', async (conv) => {
    const data = await getContentFromAPI();
    conv.close(new SimpleResponse(data));
});

exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);
