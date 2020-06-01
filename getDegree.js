import * as dynamoDbLib from "./libs/dynamodb-lib";
import {success, failure} from "./libs/response-lib";

export async function main(event, context) {
    console.log(event);

    const params = {
        TableName: process.env.bcadminDegree,
        KeyConditionExpression: "degree = :degree",
        ExpressionAttributeValues: {
            ":degree": event.pathParameters.degree
        }
    };

    try {
        const result = await dynamoDbLib.call("query", params);
        console.log(result);
        if (result.Item) {
            return success(result.Item);
        }
        else if (result.Items) {
            return success(result.Items);
        }
        else {
            return failure({status: false, error: "Item not found"});
        }
    }
    catch (e) {
        console.log(e);
        return failure({status: false});
    }
}