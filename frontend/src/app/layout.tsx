import '@mantine/core/styles.css'
import './styles.css'
import { ColorSchemeScript, Container } from '@mantine/core'
import { Header } from '@/components/Header'
import Providers from '@/components/Providers'

export const metadata = {
  title: 'Table Football Challenge',
  description: '',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <ColorSchemeScript />
      </head>
      <body>
        <Providers>
          <Container size="md">
            <Header />
            {children}
          </Container>
        </Providers>
      </body>
    </html>
  )
}
