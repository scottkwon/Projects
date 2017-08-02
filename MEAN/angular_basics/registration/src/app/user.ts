export class User {
    constructor(
        public id: number = null,
        public firstName: string = "",
        public lastName: string = "",
        public email: string = "",
        public password: any = "",
        public passwordConfirmation: any = "",
        public streetAddress: any = "",
        public unit: number = null,
        public city: string = "",
        public state: string = "",
        public lucky: string = "" ,
        public created_at: Date = new Date(),
        public updated_at: Date = new Date()
    ){};
}