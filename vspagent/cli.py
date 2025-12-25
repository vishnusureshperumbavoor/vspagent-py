"""VSP Agent - CLI Interface"""

import sys
import io
from .agent import VSPAgent

# Fix Windows console encoding
if sys.platform == 'win32':
    try:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    except:
        pass


def main():
    """Main CLI entry point"""
    print("=" * 62)
    print("          🤖  VSP Agent - Interactive Chat Mode")
    print("              Powered by Qwen2.5-0.5B AI")
    print("=" * 62)
    print()
    
    agent = VSPAgent()
    
    try:
        agent.init_ai()
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Try: pip install transformers torch")
        return
    
    print("\n✅ VSP Agent is ready to chat!\n")
    print("Type 'exit' or 'quit' to end the conversation.\n")
    
    conversation_history = []
    
    while True:
        try:
            user_input = input("💬 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['exit', 'quit']:
                print("\n👋 Thanks for chatting with VSP Agent! Goodbye! 🚀\n")
                break
            
            # Get AI response
            response = agent.chat(user_input, conversation_history)
            
            # Update history
            conversation_history.append({"role": "user", "content": user_input})
            conversation_history.append({"role": "assistant", "content": response})
            
            print(f"\n🤖 VSP Agent: {response}\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!\n")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")


if __name__ == "__main__":
    main()

