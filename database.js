import { MongoClient, ServerApiVersion } from 'mongodb';
//import 'dotenv/config';

//How to implement groupMembers

export class Database {
    constructor(dburl) {
        this.dburl = dburl;
    }

    async connect() {
        this.client = await MongoClient.connect(this.dburl, {
            useNewUrlParser: true,
            useUnifiedTopology: true,
            serverApi: ServerApiVersion.v1,
          });

        this.db = this.client.db('healthAppDatabase');

        await this.init();
    }

    async init() {
        this.collection = this.db.collection('person');
        this.collection2 = this.db.collection('group');
        this.collection3 = this.db.collection('group_members')
        const count = await this.collection.countDocuments();
    }

    async close() {
        this.client.close();
    }

    //Functions for persons
    async getAllPeople() {
        return await this.collection.find({}).toArray();
    }

    //So do you want to find out all of them or just one of them?
    async getPersonFirstName(pFirstName) {
        return await this.collection.findOne({ "pFirstName": pFirstName });
    }

    async getPersonLastName(pLastName) {
        return await this.collection.findOne({ "pLastName": pLastName });
    }

    async getPersonPoints(pPoints) {
        return await this.collection.findOne({ "pPoints": pPoints });
    }

    async getPersonTime(pTime) {
        return await this.collection.findOne({ "pTime": pTime });
    }

    async getPersonGroup(groupID) {
        return await this.collection.findOne({ "groupID": groupID });
    }

    //Functions for groups
    async getAllGroups() {
        return await this.collection2.find({}).toArray();
    }

    async getGroupGoal(groupGoal) {
        return await this.collection2.findOne({ "groupGoal": groupGoal });
    }

    async getGroupAchieved(achieved) {
        return await this.collection2.findOne({ "achieved": achieved });
    }

    async getGroupPoints(groupPoints) {
        return await this.collection2.findOne({ "groupPoints": groupPoints });
    }

    async getGroupGoal(groupTime) {
        return await this.collection2.findOne({ "groupTime": groupTime });
    }

    async getGroupID(groupID) {
        return await this.collection2.findOne({ "groupID": groupID });
    }
    //Functions for Group Members
    async getGroupFirstName(gMemberFN) {
        return await this.collection3.findOne({ "gMemberFN": gMemberFN });
    }

    async getGroupLastName(gMemberLN) {
        return await this.collection3.findOne({ "gMemberLN": gMemberLN });
    }

    async getGroupMemID(gMemberID) {
        return await this.collection3.findOne({ "gMemberID": gMemberID });
    }


    //Adding Functions
    async addPersonRecord(record) {
        await this.collection.insertOne(record);
    }

    async addGroupRecord(record) {
        await this.collection2.insertOne(record);
    }

    async addMemberRecord(record) {
        await this.collection3.insertOne(record);
    }

    //End of Main Portion of the File






    //Other functions - extra
    async addPersonRecord(record) {
        await this.collection.insertOne(record);
    }

    async updateTask(taskName, task) {
        await this.collection.updateOne({ "name": taskName }, { $set: task });
    }

    async deleteTask(taskName) {
        await this.collection.deleteOne({ "name": taskName });
    }

    async getAllTasksByPriority(taskPriority) {
        return await this.collection.find({ "priority": `${taskPriority}` }).toArray();
    }

    async getAllTasksByCompleted(taskCompleted) {
        return await this.collection.find({ "completed": `${taskCompleted}` }).toArray();
    }

}