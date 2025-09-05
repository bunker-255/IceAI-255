# AIexpert - AI for Autonomous Linux Server Management

AIexpert is an advanced artificial intelligence system designed for autonomous and simplified Linux server management. The system provides comprehensive monitoring of security, functionality, and fault tolerance, allowing server management through simple natural language commands.

## 🌟 Key Features

- **🔒 Security Monitoring**: Automated system auditing, vulnerability tracking, and security assurance
- **📊 Resource Management**: Real-time monitoring of CPU, memory, disk space, and network activity
- **⚡ Autonomous Management**: Execution of any Python and Bash commands through natural language
- **🛡️ Fault Tolerance**: System diagnostics and recovery capabilities
- **💾 Memory & Context**: Preservation of dialogue history and contextual system understanding
- **📈 Analytics**: Generation of performance, security, and diagnostic reports

## 🏗️ Project Architecture

```
AIexpert/
├── chat.py              # Interactive chat for server management
├── guard.py             # Security and monitoring system
├── launcher             # System startup script
├── requirements.txt     # Project dependencies
├── src/                 # Core code
│   ├── BASE.py         # AI core with Zai class
│   └── tools.py        # Utility functions
├── brain_data/          # Memory and data system
├── conversation/        # Dialogue history
└── security_reports/    # Security reports
```

### System Components

#### `chat.py` - Interactive Interface
Main module for AI communication through command line. Allows:
- Communication with AI in natural language
- Execution of Python and Bash commands
- Dialogue history preservation
- Automatic processing of execution results

#### `guard.py` - Security System
Module responsible for security and monitoring:
- Continuous system monitoring
- Automatic threat detection
- Security report generation
- Incident response

#### `src/BASE.py` - AI Core
Contains the main `Zai` class with functionality:
- Natural language processing
- Command execution
- System memory management
- Resource monitoring
- Integration with various APIs

#### `src/tools.py` - Utility Functions
Utilities for system operations:
- Data serialization/deserialization
- File and directory operations
- Event logging

## 🚀 Installation and Setup

### Requirements
- Python 3.7+
- Linux system
- Internet connection
- Root access (for some functions)

### Install Dependencies

```bash
# Clone the repository
git clone https://github.com/bunker-255/IceAI-255
cd AIexpert

# Install dependencies
pip install -r requirements.txt
```

### Configure API Keys

The system uses multiple API keys for operation. Configuration is done in `src/BASE.py`:

```python
api_key = {
    "zai": {
        "your_account": "your_api_key"
    }
}
```

### Start the System

```bash
# Start via launcher
./launcher

# Or direct launch
python3 chat.py
```

## 💡 Usage

### Basic Interaction

After starting the system, you'll see the `[USER]` prompt. Simply write a command in natural language:

```
[USER] check system load
[ACTION] Checking system load...
[SYSTEM] CPU: 15%, Memory: 45%, Disk: 67%
```

### Command Examples

#### System Monitoring
- "show system resources"
- "check free disk space"
- "monitor network"
- "run system diagnostics"

#### File Management
- "create backup of important configs"
- "find error logs"
- "clean temporary files"

#### Security
- "check system security"
- "run port audit"
- "check security updates"
- "generate security report"

#### Command Execution
- "install nginx"
- "restart service"
- "configure firewall"

### Security System

The `guard.py` module operates in background mode:
- Automatically scans system for vulnerabilities
- Monitors open ports and active processes
- Checks integrity of important files
- Generates security reports

### Memory and Context

The system saves:
- Dialogue history
- System state
- Executed commands
- Generated reports

All data is stored in the `brain_data/` directory and automatically updated.

## 🔧 Technical Details

### "Mind Navbar" System

The `Zai` class uses a unique `mind_navbar` system for contextual understanding:
- Current system resources
- File system structure
- Dialogue history
- Time and execution context

### Command Execution

The system supports two types of commands:
- **Python commands**: For complex operations and data analysis
- **Bash commands**: For system management

```python
# Python command example
{
    "type": "python",
    "content": "import psutil; print(psutil.cpu_percent())",
    "title": "CPU load check"
}

# Bash command example
{
    "type": "bash", 
    "content": "df -h",
    "title": "Disk space check"
}
```

### Logging

All system actions are logged to:
- `conversation/chat/` - chat history
- `conversation/guard/` - security events
- `brain_data/security_reports/` - security reports

## 📊 Reports and Analytics

The system automatically generates reports:
- **System Diagnostics**: Hardware and software status
- **Security Audit**: Vulnerability detection
- **Performance**: System operation metrics
- **Internet Connection**: Speed and quality

All reports are saved in Markdown format and available in the `brain_data/diagnostic_reports/` directory.

## 🔒 Security

- All API keys are stored encrypted
- Command execution occurs in isolated environment
- System has built-in security checks
- Automatic detection of suspicious activity

## 🛠️ Development

### Code Structure

- **Modular architecture**: Each component has clear responsibility
- **Extensibility**: Easy addition of new features
- **Testing**: Built-in functionality verification system

### Adding New Features

1. Create new module in `src/` directory
2. Add functionality to `Zai` class
3. Update instructions in `src/BASE.py`
4. Add tests

## 📋 System Requirements

- Operating System: Linux (Ubuntu/Debian recommended)
- Python: 3.7 or higher
- Memory: minimum 512MB RAM
- Disk: minimum 1GB free space
- Internet: for API operations and updates

## 🤝 Contributing

The project is under active development. We welcome:
- Improvement suggestions
- Bug reports
- New features
- Documentation

## 📄 License

This project is licensed under MIT. See LICENSE file for details.

## 📞 Support

For questions and support, please contact:
- Creator: Ilya Lazarev
- Email: bunker255il@gmail.com

---

**AIexpert** - Your intelligent assistant for Linux server management 🚀
