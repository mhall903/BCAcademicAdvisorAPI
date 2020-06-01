import {success} from "./libs/response-lib";
import * as dynamoDbLib from "./libs/dynamodb-lib";

export async function main(event, context, callback) {
    for(var degreeItem in event.Degrees) {
        var tableInsert = {
            TableName: "bcadmin-degree",
            Item: {
                degree: event.Degrees[degreeItem].degree,
                requirements: event.Degrees[degreeItem].requirements,
            }
        };
        try {
            await dynamoDbLib.call("put", tableInsert);
        }
        catch (e){
            console.log(e);
        }
    }

    return success({status: true});
}