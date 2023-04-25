$(function () {
  // Reference to the chat messages area
  const $chatWindow = $('#messages');

  // Our interface to the Chat service
  let chatClient;

  // A handle to the room's chat channel
  let roomChannel;

  // The server will assign the client a random username - stored here
  let username;

  // Helper function to print info messages to the chat window
  function print(infoMessage, asHtml) {
    const $msg = $('<div class="info">');
    if (asHtml) {
      $msg.html(infoMessage);
    } else {
      $msg.text(infoMessage);
    }
    $chatWindow.append($msg);
  }

  // Helper function to print chat message to the chat window
  function printMessage(fromUser, message) {
    const $user = $('<span class="username">').text(fromUser + ':');
    if (fromUser === username) {
      $user.addClass('me');
    }
    const $message = $('<span class="message">').text(message);
    const $container = $('<div class="message-container">');
    $container.append($user).append($message);
    $chatWindow.append($container);
    $chatWindow.scrollTop($chatWindow[0].scrollHeight);
  }

  // Get an access token for the current user, passing a device ID
  // for browser-based apps, we'll just use the value "browser"
  $.getJSON(
    '/chat/token', // TODO: Make sure the link for chat is verified from `chat.urls`.
    {
      device: 'browser',
    },
    function (data) {
      // Alert the user they have been assigned a random username
      username = data.identity;
      print('<span class="me">' + username + '</span>', true);

      // Initialize the Chat client
      // chatClient = new Twilio.Chat.Client(data.token);

      Twilio.Chat.Client.create(data.token).then((client) => {
        // Use client
        chatClient = client;
        chatClient
          .getSubscribedChannels()
          .then(createOrJoinChannel(data.channel_name)); //
      });
    },
  );

  function hasJoinedChannel(name) {
    // Check if member has already joined this channel name
    chatClient.getUserChannelDescriptors().then(function (paginator) {
      for (i = 0; i < paginator.items.length; i++) {
        const channel = paginator.items[i];
        if (channel.uniqueName == name) {
          console.log(`Found channel... `);
          return true;
        }
      }
    });
    return false;
  }

  // Set up channel after it has been found / created
  function setupChannel(name) {
    roomChannel
      .join()
      .then(function (channel) {
        print(
          `Joined channel ${name} as <span class="me"> ${username} </span>.`,
          true,
        );
        channel.getMessages(30).then(processPage);
      })
      .catch(function (err) {
        if (err.code == 50404) {
          console.log(`Error while setting up the channel: ${err.message}`);
        }
      });

    // Listen for new messages sent to the channel
    roomChannel.on('messageAdded', function (message) {
      printMessage(message.author, message.body);
    });
  }

  function processPage(page) {
    page.items.forEach((message) => {
      printMessage(message.author, message.body);
    });
    if (page.hasNextPage) {
      page.nextPage().then(processPage);
    } else {
      console.log('Done loading messages');
    }
  }

  function createOrJoinChannel(channelName) {
    print(`Attempting to join "${channelName}" chat channel...`);
    chatClient
      .getChannelByUniqueName(channelName)
      .then(function (channel) {
        roomChannel = channel;
        try{

           // IF member has already joined then we will be able to read the messages on that channel.
        roomChannel.getMessages(30).then(processPage);
        // Listen for new messages sent to the channel
        roomChannel.on('messageAdded', function (message) {
          printMessage(message.author, message.body);
        });

        } catch (err)
        {
          console.error(`Member has not joined... ${err}`);
          setupChannel(channelName);
        }
       

        
      })
      .catch(function (err) {
        // If it doesn't exist, let's create it
        console.log('Trying to create channel for :', channelName);
        chatClient
          .createChannel({
            uniqueName: channelName,
            friendlyName: `${channelName} Chat Channel`,
          })
          .then(function (channel) {
            roomChannel = channel;
            setupChannel(channelName);
          });
      });
  }

  // Add newly sent messages to the channel
  const $form = $('#message-form');
  const $input = $('#message-input');
  $form.on('submit', function (e) {
    e.preventDefault();
    if (roomChannel && $input.val().trim().length > 0) {
      roomChannel.sendMessage($input.val());
      $input.val('');
    }
  });
});
