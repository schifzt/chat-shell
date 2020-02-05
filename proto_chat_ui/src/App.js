import React from 'react'
import MessageList from './components/MessageList'
import SendMessageForm from './components/SendMessageForm'
import RoomList from './components/RoomList'
import NewRoomForm from './components/NewRoomForm'

// import { tokenUrl, instanceLocator } from './config'

class App extends React.Component {
    constructor() {
        super()
        this.state = {
            messages: [
                {
                    senderId: 'perborgen',
                    text: 'Hey, how is it going?'
                },
                {
                    senderId: 'janedoe',
                    text: 'Great! How about you?'
                },
                {
                    senderId: 'perborgen',
                    text: 'Good to hear! I am great as well'
                }
            ]
        }
    }

    render() {
        return (
            <div className="app">
                <RoomList />
                <MessageList messages={this.state.messages} />
                <SendMessageForm />
                <NewRoomForm />
            </div>
        );
    }
}

export default App