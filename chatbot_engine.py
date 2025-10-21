# chatbot_engine.py

from knowledge_base import RITUAL_DATA

class HinduRitualChatbot:
    def __init__(self):
        """Initializes the chatbot with the knowledge base."""
        self.knowledge_base = RITUAL_DATA

    def _find_best_match(self, user_input):
        """
        Finds the best matching topic based on keywords in the user's input.
        This is a simple keyword-based search.
        """
        user_input = user_input.lower()
        best_match = None
        max_keywords_found = 0

        for topic in self.knowledge_base:
            keywords_found = 0
            for keyword in topic["keywords"]:
                if keyword.lower() in user_input:
                    keywords_found += 1
            
            # If this topic has more matching keywords, it's a better match
            if keywords_found > max_keywords_found:
                max_keywords_found = keywords_found
                best_match = topic
        
        # Return the best match if at least one keyword was found
        return best_match if max_keywords_found > 0 else None

    def get_response(self, user_input):
        """
        Processes user input and returns the appropriate response.
        """
        # Handle exit/greetings
        if user_input.lower() in ["quit", "exit", "bye"]:
            return "Goodbye! May you be blessed."

        # Find the relevant topic from the knowledge base
        best_match = self._find_best_match(user_input)

        if best_match:
            response = f"--- {best_match['topic']} ---\n\n"
            response += best_match['rules']
            return response
        else:
            # Fallback response if no topic is found
            response = "I'm sorry, I don't have information on that topic. "
            response += "I can tell you about:\n"
            from knowledge_base import get_available_topics
            for topic in get_available_topics():
                response += f"- {topic}\n"
            response += "Please ask about one of these."
            return response
