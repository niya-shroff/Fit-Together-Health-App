import express from 'express';
import logger from 'morgan';
import cors from 'cors'; 
/* 
The cors import is used to enable CORS (Cross-Origin Resource Sharing), 
which allows us to send a request from the front-end hosted on one port 
to a back-end hosted on another port for testing purposes. Redundant in prod.
*/
import { Database } from './database.js';

class Server {
    constructor(dburl) {
        this.dburl = dburl;
        this.app = express();
        this.app.use(express.json());
        this.app.use(express.urlencoded({ extended: false }));
        this.app.use(logger('dev'));
        this.app.use('/', express.static('client'));
        this.app.use(cors());
    }

    async initRoutes() {
        const self = this;
        //Main functions for get
        this.app.get('/test', (req, res) => {
            res.send('Hello World!');
        });

        //Functions for Person
        this.app.get('/api/people/all', async (req, res) => {
            const tasks = await self.db.getAllPeople();
            res.send(tasks);
        });

        this.app.get('/api/people/personfn', async (req, res) => {
            const tasks = await self.db.getPersonFirstName();
            res.send(tasks);
        });

        this.app.get('/api/people/personln', async (req, res) => {
            const tasks = await self.db.getPersonLastName();
            res.send(tasks);
        });

        this.app.get('/api/people/personpoints', async (req, res) => {
            const tasks = await self.db.getPersonPoints();
            res.send(tasks);
        });

        this.app.get('/api/people/persontime', async (req, res) => {
            const tasks = await self.db.getPersonTime();
            res.send(tasks);
        });

        this.app.get('/api/people/persongroup', async (req, res) => {
            const tasks = await self.db.getPersonGroup();
            res.send(tasks);
        });

        //Functions for group
        this.app.get('/api/people/groupgoal', async (req, res) => {
            const tasks = await self.db.getGroupGoal();
            res.send(tasks);
        });

        this.app.get('/api/people/groupachieve', async (req, res) => {
            const tasks = await self.db.getGroupAchieve();
            res.send(tasks);
        });

        this.app.get('/api/people/grouppoints', async (req, res) => {
            const tasks = await self.db.getGroupPoints();
            res.send(tasks);
        });

        this.app.get('/api/people/grouptime', async (req, res) => {
            const tasks = await self.db.getGroupTime();
            res.send(tasks);
        });

        this.app.get('/api/people/groupid', async (req, res) => {
            const tasks = await self.db.getGroupID();
            res.send(tasks);
        });

        //Functions for Group Members
        this.app.get('/api/people/groupmemid', async (req, res) => {
            const tasks = await self.db.getGroupMemID();
            res.send(tasks);
        });

        this.app.get('/api/people/groupfn', async (req, res) => {
            const tasks = await self.db.getGroupFirstName();
            res.send(tasks);
        });

        this.app.get('/api/people/groupln', async (req, res) => {
            const tasks = await self.db.getGroupLastName();
            res.send(tasks);
        });


        //Main functions for Adding
        this.app.post('/api/tasks/person-record', async (req, res) => {
            const task = await self.db.addPersonRecord(req.body);
            res.send(task);
        });

        this.app.post('/api/tasks/group-record', async (req, res) => {
            const task = await self.db.addGroupRecord(req.body);
            res.send(task);
        });

        this.app.post('/api/tasks/member-record', async (req, res) => {
            const task = await self.db.addMemberRecord(req.body);
            res.send(task);
        });

        //End of Main Portion of Insert









        //Other functions
        this.app.get('/api/tasks/:name', async (req, res) => {
            try{
                const name = req.params.name;
                const task = await self.db.getTask(name);
                res.send(task);
            } catch(err) {
                res.status(404).send(err);
            }
        });

        this.app.post('/api/tasks', async (req, res) => {
            const task = await self.db.addTask(req.body);
            res.send(task);
        });

        this.app.put('/api/tasks/:name', async (req, res) => {
            const name = req.params.name;
            const task = await self.db.updateTask(name, req.body);
            res.send(task);
        });
        
        this.app.delete('/api/tasks/:name', async (req, res) => {
            const name = req.params.name;
            const task = await self.db.deleteTask(name);
            res.send(task);
        });

        this.app.get('/api/tasks/priority/:priority', async (req, res) => {
            const tasks = await self.db.getAllTasksByPriority(req.params.priority);
            res.send(tasks);
        });

        this.app.get('/api/tasks/completed/:completed', async (req, res) => {
            const tasks = await self.db.getAllTasksByCompleted(req.params.completed);
            res.send(tasks);
        });
    }
    async initDb() {
        this.db = new Database(this.dburl);
        await this.db.connect();
    }

    async start() {
        await this.initDb();
        await this.initRoutes();
        const port = process.env.PORT || 3000;
        this.app.listen(port, () => {
            console.log(`Server listening on port ${port}`);
        });
    }
}

const server = new Server("mongodb+srv://garvind:xy6UZHYfulSSYD6w@healthappdatabase.nleazb1.mongodb.net/?retryWrites=true&w=majority");
server.start();